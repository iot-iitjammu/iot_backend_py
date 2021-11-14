import logging
from typing import Dict, Callable, List
from pydantic import parse_obj_as

from dashboard.schemas import (
    ElectricalDataSchema, FetchHistogramInput, TimestampAndValueObjectSchema
)
from dashboard.models import ElectricalData
from dashboard.constants import Periods
from dashboard.services.utils import (
    GetDayStartingTS, GetPastFirstDayOfMonthTS, GetPastMondayTS,
    GroupDailyPowerData, GroupWeeklyPowerData, GroupMonthlyPowerData,
)

logger = logging.getLogger(__name__)

def getPowerHistogram(input_obj: FetchHistogramInput) -> List[TimestampAndValueObjectSchema]:
    input_obj.ToTimeStamp = input_obj.Timestamp

    round_ts_mapping_func: Dict[str, Callable[[int], int]] = {
        Periods.DailyGroup: GetDayStartingTS,
        Periods.WeeklyGroup: GetPastMondayTS,
        Periods.MonthlyGroup: GetPastFirstDayOfMonthTS,
    }

    input_obj.FromTimeStamp = round_ts_mapping_func[input_obj.Period](
        input_obj.ToTimeStamp
    )

    try:
        query_set = ElectricalData.objects.filter(
            client_id=input_obj.ClientId,
            delete_status=not True,
            generation_time_stamp__gte=input_obj.FromTimeStamp,
            generation_time_stamp__lt=input_obj.ToTimeStamp
        )
    except Exception as e:
        logger.error(f'FetchPowerHistogram Error: {e}')       
        return None

    samples = parse_obj_as(List[ElectricalDataSchema], list(query_set))

    group_mapping: Dict[
        str,
        Callable[[List[ElectricalDataSchema]], List[TimestampAndValueObjectSchema]]
    ] = {
        Periods.DailyGroup: GroupDailyPowerData,
        Periods.WeeklyGroup: GroupWeeklyPowerData,
        Periods.MonthlyGroup: GroupMonthlyPowerData,
    }

    try:
        grouped_samples = group_mapping[input_obj.Period](samples)
    except Exception as e:
        logger.error(f'FetchPowerHistogram Error: {e}')       
        return None

    return grouped_samples
