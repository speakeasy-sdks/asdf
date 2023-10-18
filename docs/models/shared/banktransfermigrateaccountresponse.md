# BankTransferMigrateAccountResponse

Defines the response schema for `/bank_transfer/migrate_account`


## Fields

| Field                                                                                                                                       | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                     | Dict[str, *Any*]                                                                                                                            | :heavy_minus_sign:                                                                                                                          | N/A                                                                                                                                         |
| `access_token`                                                                                                                              | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | The Plaid `access_token` for the newly created Item.                                                                                        |
| `account_id`                                                                                                                                | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | The Plaid `account_id` for the newly created Item.                                                                                          |
| `request_id`                                                                                                                                | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |