from django.http import HttpResponse, HttpRequest
from django.views import View
from pydantic import ValidationError

from dashboard.schemas import FetchHistogramInput
from dashboard.services.GetHistogram import getPowerHistogram 


# Create your views here.

class PowerHistogramView(View):
    
    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            req = FetchHistogramInput.parse_raw(
                request.body,
                content_type=request.content_type
            )
        except ValidationError as e:
            print(e.json())
            return HttpResponse("Bad Request", status=400)

        print(req)

        getPowerHistogram(req)

        return HttpResponse(req.json(), content_type="application/json")
