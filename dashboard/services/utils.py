from datetime import datetime, timedelta
from dashboard.schemas import ElectricalDataSchema, TimestampAndValueObjectSchema
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


def GroupDailyPowerData(samples: List[ElectricalDataSchema]) -> List[TimestampAndValueObjectSchema]:
    grouped_data = []

    tsToSampleMap: DefaultDict[int, List[ElectricalDataSchema]] = defaultdict(list)

    for sample in samples:
        hourTS = GetRoundOffHourTS(sample.GenerationTimeStamp)
        tsToSampleMap[hourTS].append(sample)

    for ts, ts_samples in tsToSampleMap.items():
        # division to be checked
        avg_power = sum([sample.AveragePower for sample in ts_samples]) / len(ts_samples)
        grouped_data.append(TimestampAndValueObjectSchema.construct(
            Timestamp=ts,
            Value=avg_power
        ))

    return grouped_data


def GroupWeeklyPowerData(samples: List[ElectricalDataSchema]) -> List[TimestampAndValueObjectSchema]:
    grouped_data = []

    tsToSampleMap: DefaultDict[int, List[ElectricalDataSchema]] = defaultdict(list)

    for sample in samples:
        dayTS = GetRoundOffDayTS(sample.GenerationTimeStamp)
        tsToSampleMap[dayTS].append(sample)

    for ts, ts_samples in tsToSampleMap.items():
        avg_power = sum([sample.AveragePower for sample in ts_samples]) / len(ts_samples)
        grouped_data.append(TimestampAndValueObjectSchema(
            Timestamp=ts,
            Value=avg_power
        ))

    return grouped_data


def GroupMonthlyPowerData(samples: List[ElectricalDataSchema]) -> List[TimestampAndValueObjectSchema]:
    grouped_data = []

    tsToSampleMap: DefaultDict[int, List[ElectricalDataSchema]] = defaultdict(list)

    for sample in samples:
        monthTS = GetRoundOffMonthTS(sample.GenerationTimeStamp)
        tsToSampleMap[monthTS].append(sample)

    for ts, ts_samples in tsToSampleMap.items():
        avg_power = sum([sample.AveragePower for sample in ts_samples]) / len(ts_samples)
        grouped_data.append(TimestampAndValueObjectSchema(
            Timestamp=ts,
            Value=avg_power
        ))

    return grouped_data


def GroupDailyEnergyData(samples: List[ElectricalDataSchema]) -> List[TimestampAndValueObjectSchema]:
    grouped_data = []

    tsToSampleMap: DefaultDict[int, List[ElectricalDataSchema]] = defaultdict(list)

    for sample in samples:
        hourTS = GetRoundOffHourTS(sample.GenerationTimeStamp)
        tsToSampleMap[hourTS].append(sample)

    for ts, ts_samples in tsToSampleMap.items():

        avg_power = sum([sample.EnergyConsumption for sample in ts_samples]) / len(ts_samples)
        grouped_data.append(TimestampAndValueObjectSchema.construct(
            Timestamp=ts,
            Value=avg_power
        ))

    return grouped_data


def GroupWeeklyEnergyData(samples: List[ElectricalDataSchema]) -> List[TimestampAndValueObjectSchema]:
    grouped_data = []

    tsToSampleMap: DefaultDict[int, List[ElectricalDataSchema]] = defaultdict(list)

    for sample in samples:
        dayTS = GetRoundOffDayTS(sample.GenerationTimeStamp)
        tsToSampleMap[dayTS].append(sample)

    for ts, ts_samples in tsToSampleMap.items():
        avg_power = sum([sample.EnergyConsumption for sample in ts_samples]) / len(ts_samples)
        grouped_data.append(TimestampAndValueObjectSchema.construct(
            Timestamp=ts,
            Value=avg_power
        ))

    return grouped_data


def GroupMonthlyEnergyData(samples: List[ElectricalDataSchema]) -> List[TimestampAndValueObjectSchema]:
    grouped_data = []

    tsToSampleMap: DefaultDict[int, List[ElectricalDataSchema]] = defaultdict(list)

    for sample in samples:
        monthTS = GetRoundOffMonthTS(sample.GenerationTimeStamp)
        tsToSampleMap[monthTS].append(sample)

    for ts, ts_samples in tsToSampleMap.items():
        avg_power = sum([sample.EnergyConsumption for sample in ts_samples]) / len(ts_samples)
        grouped_data.append(TimestampAndValueObjectSchema.construct(
            Timestamp=ts,
            Value=avg_power
        ))

    return grouped_data
