# Credit1099Payer

An object representing a payer used by 1099-MISC tax documents.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `additional_properties`                                                              | Dict[str, *Any*]                                                                     | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `address`                                                                            | [Optional[shared.CreditPayStubAddress]](../../models/shared/creditpaystubaddress.md) | :heavy_minus_sign:                                                                   | Address on the pay stub.                                                             |
| `name`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Name of payer.                                                                       |
| `telephone_number`                                                                   | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Telephone number of payer.                                                           |
| `tin`                                                                                | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Tax identification number of payer.                                                  |