import datetime


class DeviceCode:
    def __init__(
            self, device_code: str, expires_in: str, interval: str, user_code: str, verification_uri: str,
            verification_uri_full: str
    ):
        self.device_code = device_code
        self.expires_in = self._str_to_td(expires_in)
        self.interval = self._str_to_td(interval)
        self.user_code = user_code
        self.verification_uri = verification_uri
        self.verification_uri_full = verification_uri_full

    @staticmethod
    def _str_to_td(string: str) -> datetime.timedelta:
        t = datetime.datetime.strptime(string, "%H:%M:%S")
        return datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
