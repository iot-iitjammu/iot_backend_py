from datetime import datetime, timedelta
from dashboard.schemas import ElectricalData, TimestampAndValueObject
from typing import List, DefaultDict
from collections import defaultdict

def GetDayStartingTS(ts: int) -> int:
    dateObj = datetime.fromtimestamp(ts)
    starting_date = datetime(dateObj.year, dateObj.month, dateObj.day)
    return int(starting_date.timestamp())

def GetPastFirstDayOfMonthTS(ts: int) -> int:
    dateObj = datetime.fromtimestamp(ts)
    starting_date = datetime(dateObj.year, dateObj.month, 1)
    return int(starting_date.timestamp())

def GetPastMondayTS(ts: int) -> int:
    dateObj = datetime.fromtimestamp(ts)
    starting_date = datetime(dateObj.year, dateObj.month, dateObj.day)
    while starting_date.weekday() != 0:
        starting_date -= timedelta(days=1)
    return int(starting_date.timestamp())

def GetRoundOffHourTS(ts: int) -> int:
    dateObj = datetime.fromtimestamp(ts)
    starting_date = datetime(dateObj.year, dateObj.month, dateObj.day, dateObj.hour)
    return int(starting_date.timestamp())

def GetRoundOffDayTS(ts: int) -> int:
    dateObj = datetime.fromtimestamp(ts)
    starting_date = datetime(dateObj.year, dateObj.month, dateObj.day)
    return int(starting_date.timestamp())

def GetRoundOffMonthTS(ts: int) -> int:
    dateObj = datetime.fromtimestamp(ts)
    starting_date = datetime(dateObj.year, dateObj.month, 1)
    return int(starting_date.timestamp())


def GroupDailyPowerData(samples: List[ElectricalData]) -> List[TimestampAndValueObject]:
    grouped_data = []

    tsToSampleMap: DefaultDict[int, List[ElectricalData]] = defaultdict(list)

    for sample in samples:
        hourTS = GetRoundOffHourTS(sample.timestamp)
        tsToSampleMap[hourTS].append(sample)

    for ts, ts_samples in tsToSampleMap.items():
        avg_power = sum([sample.power for sample in ts_samples]) / len(ts_samples) # to be checked
        grouped_data.append(TimestampAndValueObject(
            timestamp=ts,
            value=avg_power
        ))

    return grouped_data

def GroupWeeklyPowerData(samples: List[ElectricalData]) -> List[TimestampAndValueObject]:
    grouped_data = []

    tsToSampleMap: DefaultDict[int, List[ElectricalData]] = defaultdict(list)

    for sample in samples:
        dayTS = GetRoundOffDayTS(sample.timestamp)
        tsToSampleMap[dayTS].append(sample)

    for ts, ts_samples in tsToSampleMap.items():
        avg_power = sum([sample.power for sample in ts_samples]) / len(ts_samples) # to be checked
        grouped_data.append(TimestampAndValueObject(
            timestamp=ts,
            value=avg_power
        ))

    return grouped_data

def GroupMonthlyPowerData(samples: List[ElectricalData]) -> List[TimestampAndValueObject]:
    grouped_data = []

    tsToSampleMap: DefaultDict[int, List[ElectricalData]] = defaultdict(list)

    for sample in samples:
        monthTS = GetRoundOffMonthTS(sample.timestamp)
        tsToSampleMap[monthTS].append(sample)

    for ts, ts_samples in tsToSampleMap.items():
        avg_power = sum([sample.power for sample in ts_samples]) / len(ts_samples) # to be checked
        grouped_data.append(TimestampAndValueObject(
            timestamp=ts,
            value=avg_power
        ))

    return grouped_data



        