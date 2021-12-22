import time
import random
import logging
from typing import List
from dashboard.schemas import ElectricalDataSchema
from dashboard.models import ElectricalData


logger = logging.getLogger(__name__)


def logElectricalData(data: ElectricalDataSchema):
    try:
        elect_data = ElectricalData(**data.dict(by_alias=True))
        elect_data.save()
    except Exception as e:
        logger.error(f'Error while logging electrical data: {e}')
        return False
    return elect_data.id


def populateDummyData() -> bool:
    total_days: int = 100
    samples_per_day: int = 96

    current_time_stamp: int = int(time.time())

    dummy_data: List[ElectricalData] = []

    for i in range(total_days*samples_per_day):
        vrms: float = 200 + 40*random.uniform(0, 1)
        irms: float = 25*random.uniform(0, 1)
        v_peak = round(random.uniform(255, 340), 3)
        i_peak = round(random.uniform(3, 12), 3)
        phase = round(random.uniform(0.555, 0.723), 3)
        v_freq = round(random.uniform(48, 51), 3)
        elec_data: ElectricalData = ElectricalData(
            client_id='test_abhis',
            generation_time_stamp=current_time_stamp - int(i*900),
            voltage_rms=vrms,
            current_rms=irms,
            voltage_peak = v_peak,
            current_peak = i_peak,
            phase = phase,
            voltage_frequency = v_freq,
            average_power=(vrms*irms)/1000,
            energy_consumption=(vrms*irms)/4000,
            delete_status=False
        )
        dummy_data.append(elec_data)

    try:
        ElectricalData.objects.insert(dummy_data)  # mongoengine.bulk_write
    except Exception as e:
        logger.error(f'Error while populating dummy data: {e}')
        return False

    return True


def deleteElectricalData() -> bool:
    try:
        ElectricalData.objects.all().delete()
    except Exception as e:
        logger.error(f'Error while deleting electrical data: {e}')
        return False

    return True
