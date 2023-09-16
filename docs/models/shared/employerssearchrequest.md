# EmployersSearchRequest

EmployersSearchRequest defines the request schema for `/employers/search`.


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_id`                                                                                                                                      | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `products`                                                                                                                                       | list[*str*]                                                                                                                                      | :heavy_check_mark:                                                                                                                               | The Plaid products the returned employers should support. Currently, this field must be set to `"deposit_switch"`.                               |
| `query`                                                                                                                                          | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | The employer name to be searched for.                                                                                                            |
| `secret`                                                                                                                                         | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.          |