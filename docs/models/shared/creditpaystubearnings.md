# CreditPayStubEarnings

An object representing both a breakdown of earnings on a pay stub and the total earnings.


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `breakdown`                                                                                         | List[[shared.PayStubEarningsBreakdown](../../models/shared/paystubearningsbreakdown.md)]            | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `total`                                                                                             | [shared.PayStubEarningsTotal](../../models/shared/paystubearningstotal.md)                          | :heavy_check_mark:                                                                                  | An object representing both the current pay period and year to date amount for an earning category. |
| `additional_properties`                                                                             | Dict[str, *Any*]                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |