import logging
from django.http import HttpResponse, HttpRequest
from django.views import View
from pydantic import ValidationError

from electrical_logger.services import populateDummyData, deleteElectricalData, logElectricalData
from dashboard.schemas import SuccessMessage, ElectricalDataSchema


logger = logging.getLogger(__name__)


class LogElectricalData(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        logger.info("Logging electrical data")
        try:
            req = ElectricalDataSchema.parse_raw(
                request.body,
                content_type=request.content_type
            )
        except ValidationError as e:
            return HttpResponse("Bad Request", status=400)

        if logElectricalData(req) != False:
            resp = SuccessMessage(
                message='Electrical data logged successfully',
                success=True
            )
        else:
            resp = SuccessMessage(
                message='Electrical data logging failed',
                success=False
            )
        
        return HttpResponse(resp.json(by_alias=True), content_type='application/json')


class PopulateElectricalData(View):

    def post(self, request: HttpRequest) -> HttpResponse:
        logger.info('Populating electrical data')
        if populateDummyData():
            resp = SuccessMessage(
                message='Electrical data populated successfully',
                success=True
            )
        else:
            resp = SuccessMessage(
                message='Electrical data population failed',
                success=False
            )
        return HttpResponse(resp.json(by_alias=True), content_type='application/json')

    def delete(self, request: HttpRequest) -> HttpResponse:
        logger.info('Deleting electrical data')
        if deleteElectricalData():
            resp = SuccessMessage(
                message='Electrical data deleted successfully',
                success=True
            )
        else:
            resp = SuccessMessage(
                message='Electrical data deletion failed',
                success=False
            )
        return HttpResponse(resp.json(by_alias=True), content_type='application/json')
