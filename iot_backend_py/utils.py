from django.http import HttpRequest, HttpResponse
from pydantic import BaseModel, ValidationError

def parseRequestHelper(req: HttpRequest, schema: BaseModel) -> dict:
    try:
        return schema.parse_raw(
            req.body,
            content_type=req.content_type
        )
    except ValidationError as e:
        return HttpResponse("Bad Request", status=400)

def parseRequest(schema):
    def decorater(func):
        def inner_wrapper(*args, **kwargs):
            parsedReq = parseRequestHelper(args[1], schema)
            if isinstance(parsedReq, schema):
                return func(args, kwargs, parsedReq)
            return parsedReq
        return inner_wrapper
    return decorater
