# DepositSwitchTargetUser

The deposit switch target user


## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                   | Dict[str, *Any*]                                                                                          | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `address`                                                                                                 | [Optional[DepositSwitchAddressData]](../../models/shared/depositswitchaddressdata.md)                     | :heavy_minus_sign:                                                                                        | The user's address.                                                                                       |
| `email`                                                                                                   | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The email address of the user.                                                                            |
| `family_name`                                                                                             | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The family name (last name) of the user.                                                                  |
| `given_name`                                                                                              | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The given name (first name) of the user.                                                                  |
| `phone`                                                                                                   | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The phone number of the user. The endpoint can accept a variety of phone number formats, including E.164. |
| `tax_payer_id`                                                                                            | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | The taxpayer ID of the user, generally their SSN, EIN, or TIN.                                            |