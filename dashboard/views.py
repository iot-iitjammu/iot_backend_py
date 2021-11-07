import logging
from django.http import HttpResponse, HttpRequest
from django.views import View
from pydantic import ValidationError

from dashboard.schemas import FetchHistogramInput, HistogramOutput
from dashboard.services.GetHistogram import getPowerHistogram


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
            print(e.json())
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
