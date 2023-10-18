# AuthGetNumbers

An object containing identifying numbers used for making electronic transfers to and from the `accounts`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by any `accounts` for which data has been requested, the array for that type will be empty.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `additional_properties`                                                   | Dict[str, *Any*]                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `ach`                                                                     | List[[NumbersACH](../../models/shared/numbersach.md)]                     | :heavy_check_mark:                                                        | An array of ACH numbers identifying accounts.                             |
| `bacs`                                                                    | List[[NumbersBACS](../../models/shared/numbersbacs.md)]                   | :heavy_check_mark:                                                        | An array of BACS numbers identifying accounts.                            |
| `eft`                                                                     | List[[NumbersEFT](../../models/shared/numberseft.md)]                     | :heavy_check_mark:                                                        | An array of EFT numbers identifying accounts.                             |
| `international`                                                           | List[[NumbersInternational](../../models/shared/numbersinternational.md)] | :heavy_check_mark:                                                        | An array of IBAN numbers identifying accounts.                            |