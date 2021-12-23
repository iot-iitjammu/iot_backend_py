import logging
from django.http import HttpResponse, HttpRequest
from django.views import View

from .services.deviceStatus import getAllDeviceStatus
from .schemas import DataMessageSchema, ReponseSchema, DeviceStatusRequestSchema
from iot_backend_py.utils import parseRequest


logger = logging.getLogger(__name__)


class DeviceStatus(View):

    @parseRequest(schema=DeviceStatusRequestSchema)
    def post(self, request: HttpRequest, parsedReq: DeviceStatusRequestSchema) -> HttpResponse:
        logger.info("DeviceStatusView called")

        allClients = getAllDeviceStatus(parsedReq.from_ts, parsedReq.to_ts)

        resp = ReponseSchema.construct(
            success=True,
            result=DataMessageSchema.construct(
                data=list(allClients),
                message="Successfully fetched the device status"
            )
        )
        return HttpResponse(resp.json(by_alias=True), content_type='application/json')
