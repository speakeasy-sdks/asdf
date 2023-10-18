# Credit1099Filer

An object representing a filer used by 1099-K tax documents.


## Fields

| Field                                                                                                                                  | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                | Dict[str, *Any*]                                                                                                                       | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |
| `address`                                                                                                                              | [Optional[CreditPayStubAddress]](../../models/shared/creditpaystubaddress.md)                                                          | :heavy_minus_sign:                                                                                                                     | Address on the pay stub.                                                                                                               |
| `name`                                                                                                                                 | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Name of filer.                                                                                                                         |
| `tin`                                                                                                                                  | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Tax identification number of filer.                                                                                                    |
| `type`                                                                                                                                 | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | One of the following values will be provided: Payment Settlement Entity (PSE), Electronic Payment Facilitator (EPF), Other Third Party |