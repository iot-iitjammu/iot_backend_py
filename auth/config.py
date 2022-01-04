from pydantic import BaseSettings


class OktaConfig(BaseSettings):
    CLIENT_ID: str
    CLIENT_SECRET: str
    REDIRECT_URI: str = "https://iot.abhis.me/auth/callback"
    URI: str = "https://dev-98721211.okta.com"

    class Config:
        env_prefix = 'OKTA_'

oktaConfig = OktaConfig()
