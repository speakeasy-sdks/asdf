# BankTransfer

Represents a bank transfer within the Bank Transfers API.


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `account_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The account ID that should be credited/debited for this bank transfer.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `ach_class`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [ACHClass](../../models/shared/achclass.md)                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Specifies the use case of the transfer. Required for transfers on an ACH network.<br/><br/>`"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts<br/><br/>`"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment<br/><br/>`"tel"` - Telephone-Initiated Entry<br/><br/>`"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet |
| `amount`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The amount of the bank transfer (decimal string with two digits of precision e.g. "10.00").                                                                                                                                                                                                                                                                                                                                                                                      |
| `cancellable`                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *bool*                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | When `true`, you can still cancel this bank transfer.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `created`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The datetime when this bank transfer was created. This will be of the form `2006-01-02T15:04:05Z`                                                                                                                                                                                                                                                                                                                                                                                |
| `custom_tag`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | A string containing the custom tag provided by the client in the create request. Will be null if not provided.                                                                                                                                                                                                                                                                                                                                                                   |
| `description`                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The description of the transfer.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `direction`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[BankTransferDirection]](../../models/shared/banktransferdirection.md)                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Indicates the direction of the transfer: `outbound` for API-initiated transfers, or `inbound` for payments received by the FBO account.                                                                                                                                                                                                                                                                                                                                          |
| `failure_reason`                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[BankTransferFailure]](../../models/shared/banktransferfailure.md)                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise.                                                                                                                                                                                                                                                                                                                                                                             |
| `id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Plaid’s unique identifier for a bank transfer.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `iso_currency_code`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The currency of the transfer amount, e.g. "USD"                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `metadata`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Dict[str, *str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:<br/>The JSON values must be Strings (no nested JSON objects allowed)<br/>Only ASCII characters may be used<br/>Maximum of 50 key/value pairs<br/>Maximum key length of 40 characters<br/>Maximum value length of 500 characters<br/>                                                                                                                     |
| `network`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [BankTransferNetwork](../../models/shared/banktransfernetwork.md)                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The network or rails used for the transfer. Valid options are `ach`, `same-day-ach`, or `wire`.                                                                                                                                                                                                                                                                                                                                                                                  |
| `origination_account_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Plaid’s unique identifier for the origination account that was used for this transfer.                                                                                                                                                                                                                                                                                                                                                                                           |
| `status`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [BankTransferStatus](../../models/shared/banktransferstatus.md)                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The status of the transfer.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [BankTransferType](../../models/shared/banktransfertype.md)                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account.                                                                                                                                                                                                                                                              |
| `user`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [BankTransferUser](../../models/shared/banktransferuser.md)                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The legal name and other information for the account holder.                                                                                                                                                                                                                                                                                                                                                                                                                     |