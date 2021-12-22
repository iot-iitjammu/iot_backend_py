from dashboard.models import ElectricalData
from devices.schemas import DeviceStatusSchema
from typing import Dict

def getAllDeviceStatus(from_ts, to_ts) -> Dict[str, DeviceStatusSchema]:
    clients = ElectricalData.objects.filter(
        delete_status=not True,
        generation_time_stamp__gte=from_ts,
        generation_time_stamp__lte=to_ts,
    ).only('client_id', 'generation_time_stamp').select_related()
    lastMsgMap: Dict[str, DeviceStatusSchema] = {}
    for client in clients:
        if lastMsgMap.get(client.client_id) is not None:
            if client.generation_time_stamp > lastMsgMap[client.client_id].LastDataTimeStamp:
                lastMsgMap[client.client_id].LastDataTimeStamp = client.generation_time_stamp
        else:
            lastMsgMap[client.client_id] = DeviceStatusSchema.construct(
                ClientId=client.client_id,
                ClientName=client.client_id,
                LastDataTimeStamp=client.generation_time_stamp
            )

    return lastMsgMap