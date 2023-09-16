# TransferBalanceGetRequest

Defines the request schema for `/transfer/balance/get`


## Fields

| Field                                                                                                                                                               | Type                                                                                                                                                                | Required                                                                                                                                                            | Description                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`                                                                                                                                                         | *Optional[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.                    |
| `originator_client_id`                                                                                                                                              | *Optional[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | Client ID of the end customer.                                                                                                                                      |
| `secret`                                                                                                                                                            | *Optional[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.                             |
| `type`                                                                                                                                                              | [Optional[TransferBalanceType]](../../models/shared/transferbalancetype.md)                                                                                         | :heavy_minus_sign:                                                                                                                                                  | The type of balance.<br/><br/>`prefunded_rtp_credits` - Your prefunded RTP credit balance with Plaid<br/>`prefunded_ach_credits` - Your prefunded ACH credit balance with Plaid |