import threading
import typing
import urllib.parse

import requests

import FCSAppAccess.exceptions as exceptions


class FCSAppAccess:
    url_base = "https://fangcloudservices.pythonanywhere.com/api/v1"

    def __init__(self, client_id: str, client_secret: str, scope: typing.Union[str, typing.List[str]]):
        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = scope

        if isinstance(self._scope, str):
            self._scope = [self._scope]

        self._access_token = None
        self._refresh_token = None

    def get_scope_string(self) -> str:
        return " ".join(self._scope)

    def set_access_token(self, access_token: str, refresh_token: str = None):
        self._access_token = access_token

        if refresh_token is not None:
            self._refresh_token = refresh_token

    def _url_encode(self, text: str) -> str:
        return urllib.parse.quote_plus(str(text))

    def client_credentials(self):
        r = requests.post(self.url_base + "/oauth2", json={
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "scope": self.get_scope_string()
        })

        if r.status_code == 400:
            if r.json()["error"] == "invalid_grant":
                raise exceptions.InvalidGrantException(
                    "The provided client_id and client_secret do not match an active application"
                )

        self._scope = r.json()["scope"].split(" ")

        self.set_access_token(r.json()["access_token"], r.json()["refresh_token"])

    def refresh_token(self):
        r = requests.post(self.url_base + "/oauth2", json={
            "grant_type": "refresh_token",
            "client_id": self._client_id,
            "access_token": self._access_token,
            "refresh_token": self._refresh_token
        })
        self.set_access_token(r.json()["access_token"], r.json()["refresh_token"])

    def get_auth_code_url(self, redirect_uri: str) -> str:
        return self.url_base + "/oauth2/code?client_id={}&redirect_uri={}&response_type=code&scope={}".format(
            self._client_id, redirect_uri, self._url_encode(self.get_scope_string())
        )

    def authorization_code(self, auth_code: str):
        r = requests.post(self.url_base + "/oauth2", json={
            "grant_type": "authorization_code",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "code": auth_code
        })
        self.set_access_token(r.json()["access_token"], r.json()["refresh_token"])

    def device_code(self):
        raise NotImplementedError("Device Code Coming Soon")

    def device_code_poll(self):
        raise NotImplementedError("Device Code Coming Soon")

    def device_code_poll_async(self) -> threading.Thread:
        t = threading.Thread(target=self.device_code_poll, daemon=True, name="FCSAppAccessSDK_DeviceCodePollThread")
        t.start()
        return t