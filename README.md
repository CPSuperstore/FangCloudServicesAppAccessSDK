# FangCloudServicesAppAccessSDK
The SDK for accessing FangCloudServices with Application Access Credentials

Support for device code auth is coming soon.

## Installation
```shell
pip install FCSAppAccessSDK
```

## Usage
Credentials are obtained from the web portal via `Project > Applications`. You must be an admin user in order to access this page.

Do not forget to enable the scopes in the web portal before attempting authentication.
```python
from FCSAppAccess import FCSAppAccess

FCSAppAccess(client_id, client_secret, ["notifi:notif:pub", "bsg:command:dequeue"])
```

Or if you only require a single scope:
```python
from FCSAppAccess import FCSAppAccess

FCSAppAccess(client_id, client_secret, "*:*:*")
```
