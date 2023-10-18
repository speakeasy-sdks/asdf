# Earnings

An object representing both a breakdown of earnings on a paystub and the total earnings.


## Fields

| Field                                                                                                                   | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                 | Dict[str, *Any*]                                                                                                        | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `breakdown`                                                                                                             | List[[EarningsBreakdown](../../models/shared/earningsbreakdown.md)]                                                     | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| ~~`subtotals`~~                                                                                                         | List[[EarningsTotal](../../models/shared/earningstotal.md)]                                                             | :heavy_minus_sign:                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible. |
| `total`                                                                                                                 | [Optional[EarningsTotal]](../../models/shared/earningstotal.md)                                                         | :heavy_minus_sign:                                                                                                      | An object representing both the current pay period and year to date amount for an earning category.                     |
| ~~`totals`~~                                                                                                            | List[[EarningsTotal](../../models/shared/earningstotal.md)]                                                             | :heavy_minus_sign:                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible. |