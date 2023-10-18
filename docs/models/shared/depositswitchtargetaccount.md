# DepositSwitchTargetAccount

The deposit switch destination account


## Fields

| Field                                                                                                                                                                                     | Type                                                                                                                                                                                      | Required                                                                                                                                                                                  | Description                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                   | Dict[str, *Any*]                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                        | N/A                                                                                                                                                                                       |
| `account_name`                                                                                                                                                                            | *str*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | The name of the deposit switch destination account, as it will be displayed to the end user in the Deposit Switch interface. It is not required to match the name used in online banking. |
| `account_number`                                                                                                                                                                          | *str*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | Account number for deposit switch destination                                                                                                                                             |
| `account_subtype`                                                                                                                                                                         | [DepositSwitchTargetAccountAccountSubtype](../../models/shared/depositswitchtargetaccountaccountsubtype.md)                                                                               | :heavy_check_mark:                                                                                                                                                                        | The account subtype of the account, either `checking` or `savings`.                                                                                                                       |
| `routing_number`                                                                                                                                                                          | *str*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | Routing number for deposit switch destination                                                                                                                                             |