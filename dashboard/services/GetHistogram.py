from dashboard.schemas import FetchHistogramInput
from dashboard.constants import Periods
from dashboard.services.utils import (
    GetDayStartingTS, GetPastFirstDayOfMonthTS, GetPastMondayTS,
    GroupDailyPowerData, GroupWeeklyPowerData, GroupMonthlyPowerData,
    )


def getPowerHistogram(input_obj: FetchHistogramInput):
    input_obj.ToTimeStamp = input_obj.Timestamp

    round_ts_mapping_func = {
        Periods.DailyGroup: GetDayStartingTS,
        Periods.WeeklyGroup: GetPastMondayTS,
        Periods.MonthlyGroup: GetPastFirstDayOfMonthTS,
    }
    
    input_obj.FromTimeStamp = round_ts_mapping_func[input_obj.Period](input_obj.ToTimeStamp)

    """
    Query the database for the data
    """
    samples = {}

    group_mapping = {
        Periods.DailyGroup: GroupDailyPowerData,
        Periods.WeeklyGroup: GroupWeeklyPowerData,
        Periods.MonthlyGroup: GroupMonthlyPowerData,
    }

    grouped_samples = group_mapping[input_obj.Period](samples)

    return grouped_samples





