import logging
from django.http import HttpResponse, HttpRequest
from django.views import View

from electrical_logger.services import populateDummyData, deleteElectricalData
from dashboard.schemas import SuccessMessage


logger = logging.getLogger(__name__)


class PopulateElectricalData(View):

    def get(self, request: HttpRequest) -> HttpResponse:
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
