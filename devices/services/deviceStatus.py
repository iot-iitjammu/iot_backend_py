from dashboard.models import ElectricalData
from devices.schemas import DeviceStatusSchema
from typing import List


def getAllDeviceStatus(from_ts, to_ts) -> List[DeviceStatusSchema]:
    clients = ElectricalData.objects.filter(
        delete_status=not True,
        timestamp__gte=from_ts,
        timestamp__lte=to_ts,
    ).only('client_id', 'timestamp').aggregate(
        {
            "$group": {
                "_id": "$client_id",
                "last_ts": {"$max": "$timestamp"}
            }
        }
    )

    clientStatus: List[DeviceStatusSchema] = []

    for client in clients:
        clientStatus.append(DeviceStatusSchema.construct(
            ClientId=client['_id'],
            ClientName=client['_id'],
            LastDataTimeStamp=client['last_ts']
        ))

    return clientStatus
