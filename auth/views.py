import logging
import requests
from django.http import HttpResponse, HttpRequest
from django.views import View
from .config import oktaConfig
from .schemas import AuthCallbackSchema, Tokens, CallbackResponse
from iot_backend_py.utils import parseRequest


logger = logging.getLogger(__name__)


import asyncio

from okta_jwt_verifier import JWTVerifier


loop = asyncio.get_event_loop()


def is_access_token_valid(token, issuer, client_id):
    jwt_verifier = JWTVerifier(issuer, client_id, 'api://default')
    try:
        loop.run_until_complete(jwt_verifier.verify_access_token(token))
        return True
    except Exception:
        return False


def is_id_token_valid(token, issuer, client_id):
    jwt_verifier = JWTVerifier(issuer, client_id, 'api://default')
    try:
        loop.run_until_complete(jwt_verifier.verify_id_token(token))
        return True
    except Exception:
        return False


class OktaAuthView(View):

    @parseRequest(AuthCallbackSchema)
    def post(self, request: HttpRequest, parsedReq: AuthCallbackSchema) -> HttpResponse:
        logger.info("Get Access Token from Okta")

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        query_params = {
            'grant_type': 'authorization_code',
            'code': parsedReq.code,
            'redirect_uri': parsedReq.redirect_uri
        }

        query_params = requests.compat.urlencode(query_params)

        exchange = requests.post(
            f"{oktaConfig.URI}/oauth2/default/v1/token",
            headers=headers,
            data=query_params,
            auth=(oktaConfig.CLIENT_ID, oktaConfig.CLIENT_SECRET),
        ).json()

        response = CallbackResponse.construct(
            status=False,
        )

        if not exchange.get("token_type"):
            response.message = "Unsupported token type. Should be 'Bearer'."
        else:
            access_token = exchange["access_token"]
            id_token = exchange["id_token"]
            issuer = oktaConfig.URI + '/oauth2/default'

            if not is_access_token_valid(access_token, issuer, oktaConfig.CLIENT_ID):
                response.message = "Access token is invalid"
            elif not is_id_token_valid(id_token, issuer, oktaConfig.CLIENT_ID):
                response.message = "ID token is invalid"
            else:
                response.message = "OK"
                response.status = True
                token = Tokens.construct(
                    id_token=id_token,
                    access_token=access_token
                )
                response.tokens = token

        return HttpResponse(response.json(exclude_unset=True), content_type='application/json')

        
