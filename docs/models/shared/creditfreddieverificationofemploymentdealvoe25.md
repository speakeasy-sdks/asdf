# CreditFreddieVerificationOfEmploymentDealVOE25

An object representing a Verification of Employment report.


## Fields

| Field                                                                                                                                                                                                    | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                  | Dict[str, *Any*]                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                       | N/A                                                                                                                                                                                                      |
| `loans`                                                                                                                                                                                                  | [CreditFreddieMacLoansVOA24](../../models/shared/creditfreddiemacloansvoa24.md)                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                       | A collection of loans that are part of a single deal.                                                                                                                                                    |
| `parties`                                                                                                                                                                                                | [CreditFreddieMacPartiesVOA24](../../models/shared/creditfreddiemacpartiesvoa24.md)                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                       | A collection of objects that define specific parties to a deal. This includes the direct participating parties, such as borrower and seller and the indirect parties such as the credit report provider. |
| `services`                                                                                                                                                                                               | [CreditFreddieMacServicesVOE25](../../models/shared/creditfreddiemacservicesvoe25.md)                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | A collection of objects that describe requests and responses for services.                                                                                                                               |