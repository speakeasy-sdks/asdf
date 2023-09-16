# ProcessorAuthGetRequest

ProcessorAuthGetRequest defines the request schema for `/processor/auth/get`


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_id`                                                                                                                                      | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `processor_token`                                                                                                                                | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: `processor-<environment>-<identifier>`      |
| `secret`                                                                                                                                         | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.          |