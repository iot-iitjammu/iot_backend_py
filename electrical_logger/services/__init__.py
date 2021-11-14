import time
import random
import logging
from typing import List
from dashboard.models import ElectricalData


logger = logging.getLogger(__name__)


def populateDummyData() -> bool:
    total_days: int = 400
    samples_per_day: int = 96

    current_time_stamp: int = int(time.time())

    dummy_data: List[ElectricalData] = []

    for i in range(total_days*samples_per_day):
        vrms: float = 200 + 40*random.uniform(0, 1)
        irms: float = 25*random.uniform(0, 1)
        elec_data: ElectricalData = ElectricalData(
            client_id='palak',
            voltage_rms=vrms,
            current_rms=irms,
            average_power=(vrms*irms)/1000,
            energy_consumption=(vrms*irms)/4000,
            generation_time_stamp=current_time_stamp - int(i*900),
            delete_status=False
        )
        dummy_data.append(elec_data)

    try:
        ElectricalData.objects.bulk_create(dummy_data)
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
