# StudentRepaymentPlan

An object representing the repayment plan for the student loan


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `description`                                                                                | *Optional[str]*                                                                              | :heavy_check_mark:                                                                           | The description of the repayment plan as provided by the servicer.                           |
| `type`                                                                                       | [Optional[shared.StudentRepaymentPlanType]](../../models/shared/studentrepaymentplantype.md) | :heavy_check_mark:                                                                           | The type of the repayment plan.                                                              |
| `additional_properties`                                                                      | Dict[str, *Any*]                                                                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |