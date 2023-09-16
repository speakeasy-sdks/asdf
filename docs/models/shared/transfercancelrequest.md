# TransferCancelRequest

Defines the request schema for `/transfer/cancel`


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_id`                                                                                                                                      | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `originator_client_id`                                                                                                                           | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).                             |
| `secret`                                                                                                                                         | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.          |
| `transfer_id`                                                                                                                                    | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | Plaid’s unique identifier for a transfer.                                                                                                        |