# TransferDiligenceSubmitRequest

Defines the request schema for `/transfer/diligence/submit`


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_id`                                                                                                                                      | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `originator_client_id`                                                                                                                           | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | Client ID of the the originator whose diligence that you want to submit.                                                                         |
| `originator_diligence`                                                                                                                           | [TransferOriginatorDiligence](../../models/shared/transferoriginatordiligence.md)                                                                | :heavy_check_mark:                                                                                                                               | The diligence information for the originator.                                                                                                    |
| `secret`                                                                                                                                         | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.          |