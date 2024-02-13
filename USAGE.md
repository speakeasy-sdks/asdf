<!-- Start SDK Example Usage [usage] -->
```python
import test_plaid
from test_plaid.models import shared

s = test_plaid.TestPlaid(
    security=shared.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.AccountsBalanceGetRequest(
    access_token='string',
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->