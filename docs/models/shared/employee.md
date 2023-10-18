# Employee

Data about the employee.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `additional_properties`                                        | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | N/A                                                            |
| `address`                                                      | [PaystubAddress](../../models/shared/paystubaddress.md)        | :heavy_check_mark:                                             | Address on the paystub                                         |
| `marital_status`                                               | *Optional[str]*                                                | :heavy_minus_sign:                                             | Marital status of the employee - either `single` or `married`. |
| `name`                                                         | *Optional[str]*                                                | :heavy_check_mark:                                             | The name of the employee.                                      |
| `taxpayer_id`                                                  | [Optional[TaxpayerID]](../../models/shared/taxpayerid.md)      | :heavy_minus_sign:                                             | Taxpayer ID of the individual receiving the paystub.           |