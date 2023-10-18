# PayrollIncomeObject

An object representing payroll data.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `additional_properties`                                     | Dict[str, *Any*]                                            | :heavy_minus_sign:                                          | N/A                                                         |
| `account_id`                                                | *Optional[str]*                                             | :heavy_check_mark:                                          | ID of the payroll provider account.                         |
| `form1099s`                                                 | List[[Credit1099](../../models/shared/credit1099.md)]       | :heavy_check_mark:                                          | Array of tax form 1099s.                                    |
| `pay_stubs`                                                 | List[[CreditPayStub](../../models/shared/creditpaystub.md)] | :heavy_check_mark:                                          | Array of pay stubs for the user.                            |
| `w2s`                                                       | List[[CreditW2](../../models/shared/creditw2.md)]           | :heavy_check_mark:                                          | Array of tax form W-2s.                                     |