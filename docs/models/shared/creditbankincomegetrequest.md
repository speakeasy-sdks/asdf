# CreditBankIncomeGetRequest

CreditBankIncomeGetRequest defines the request schema for `/credit/bank_income/get`.


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_id`                                                                                                                                      | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `options`                                                                                                                                        | [Optional[CreditBankIncomeGetRequestOptions]](../../models/shared/creditbankincomegetrequestoptions.md)                                          | :heavy_minus_sign:                                                                                                                               | An optional object for `/credit/bank_income/get` request options.                                                                                |
| `secret`                                                                                                                                         | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.          |
| `user_token`                                                                                                                                     | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | The user token associated with the User data is being requested for.                                                                             |