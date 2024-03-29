# LiabilitiesObject

An object containing liability accounts


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `credit`                                                                       | List[[shared.CreditCardLiability](../../models/shared/creditcardliability.md)] | :heavy_check_mark:                                                             | The credit accounts returned.                                                  |
| `mortgage`                                                                     | List[[shared.MortgageLiability](../../models/shared/mortgageliability.md)]     | :heavy_check_mark:                                                             | The mortgage accounts returned.                                                |
| `student`                                                                      | List[[shared.StudentLoan](../../models/shared/studentloan.md)]                 | :heavy_check_mark:                                                             | The student loan accounts returned.                                            |
| `additional_properties`                                                        | Dict[str, *Any*]                                                               | :heavy_minus_sign:                                                             | N/A                                                                            |