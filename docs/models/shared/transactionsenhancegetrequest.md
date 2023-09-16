# TransactionsEnhanceGetRequest

TransactionsEnhanceGetRequest defines the request schema for `/transactions/enhance`.


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account_type`                                                                                                                                   | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | The type of account for the requested transactions (`depository` or `credit`).                                                                   |
| `client_id`                                                                                                                                      | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret`                                                                                                                                         | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.          |
| `transactions`                                                                                                                                   | list[dict[str, *Any*]]                                                                                                                           | :heavy_check_mark:                                                                                                                               | An array of raw transactions to be enhanced.                                                                                                     |