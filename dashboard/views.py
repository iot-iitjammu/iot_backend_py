import logging
from django.http import HttpResponse, HttpRequest
from django.views import View
from pydantic import ValidationError

from dashboard.schemas import FetchHistogramInput, HistogramOutput
from dashboard.services.GetHistogram import getPowerHistogram, getEnergyHistogram


logger = logging.getLogger(__name__)


class PowerHistogramView(View):

    def post(self, request: HttpRequest) -> HttpResponse:
        logger.info("PowerHistogramView called")
        try:
            req = FetchHistogramInput.parse_raw(
                request.body,
                content_type=request.content_type
            )
        except ValidationError as e:
            return HttpResponse("Bad Request", status=400)

        grouped_sample = getPowerHistogram(req)
        if grouped_sample is not None:
            resp = HistogramOutput.construct(
                Success=True,
                Message="Successfully fetched the power histogram",
                Data=grouped_sample
            )
        else:
            resp = HistogramOutput.construct(
                Success=False,
                Message="Failed to fetch the power histogram"
            )
            
        return HttpResponse(resp.json(by_alias=True), content_type="application/json")


class EnergyHistogramView(View):

    def post(self, request: HttpRequest) -> HttpResponse:
        logger.info("EnergyHistogramView called")
        try:
            req = FetchHistogramInput.parse_raw(
                request.body,
                content_type=request.content_type
            )
        except ValidationError as e:
            return HttpResponse("Bad Request", status=400)

        grouped_sample = getEnergyHistogram(req)

        if grouped_sample is not None:
            resp = HistogramOutput.construct(
                Success=True,
                Message="Successfully fetched the energy histogram",
                Data=grouped_sample
            )
        else:
            resp = HistogramOutput.construct(
                Success=False,
                Message="Failed to fetch the energy histogram"
            )
            
        return HttpResponse(resp.json(by_alias=True), content_type="application/json")
