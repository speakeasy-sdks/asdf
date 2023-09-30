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
    client_id='Bacon',
    options=shared.AccountsBalanceGetRequestOptions(
        account_ids=[
            'Blues',
        ],
        min_last_updated_datetime=dateutil.parser.isoparse('2022-09-07T02:18:16.768Z'),
    ),
    secret='Fermium payment',
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->