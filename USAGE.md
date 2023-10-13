<!-- Start SDK Example Usage -->


```python
import test_plaid
import dateutil.parser
from test_plaid.models import shared

s = test_plaid.TestPlaid(
    security=shared.Security(
        client_id="",
        plaid_version="",
        secret="",
    ),
)

req = shared.AccountsBalanceGetRequest(
    access_token='Alafaya Loan',
    options=shared.AccountsBalanceGetRequestOptions(
        account_ids=[
            'Conroe',
        ],
    ),
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->