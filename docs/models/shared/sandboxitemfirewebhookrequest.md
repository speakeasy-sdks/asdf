# SandboxItemFireWebhookRequest

SandboxItemFireWebhookRequest defines the request schema for `/sandbox/item/fire_webhook`


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `access_token`                                                                                                                                   | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | The access token associated with the Item data is being requested for.                                                                           |
| `client_id`                                                                                                                                      | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret`                                                                                                                                         | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.          |
| `webhook_code`                                                                                                                                   | [SandboxItemFireWebhookRequestWebhookCode](../../models/shared/sandboxitemfirewebhookrequestwebhookcode.md)                                      | :heavy_check_mark:                                                                                                                               | The webhook codes that can be fired by this test endpoint.                                                                                       |
| `webhook_type`                                                                                                                                   | [Optional[WebhookType]](../../models/shared/webhooktype.md)                                                                                      | :heavy_minus_sign:                                                                                                                               | The webhook types that can be fired by this test endpoint.                                                                                       |