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
    access_token='corrupti',
    client_id='provident',
    options=shared.AccountsBalanceGetRequestOptions(
        account_ids=[
            'distinctio',
        ],
        min_last_updated_datetime=dateutil.parser.isoparse('2021-03-11T23:22:42.658Z'),
    ),
    secret='nulla',
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->