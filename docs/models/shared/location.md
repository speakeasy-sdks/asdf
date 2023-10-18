# Location

A representation of where a transaction took place


## Fields

| Field                                                                                                                     | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                   | Dict[str, *Any*]                                                                                                          | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `address`                                                                                                                 | *Optional[str]*                                                                                                           | :heavy_check_mark:                                                                                                        | The street address where the transaction occurred.                                                                        |
| `city`                                                                                                                    | *Optional[str]*                                                                                                           | :heavy_check_mark:                                                                                                        | The city where the transaction occurred.                                                                                  |
| `country`                                                                                                                 | *Optional[str]*                                                                                                           | :heavy_check_mark:                                                                                                        | The ISO 3166-1 alpha-2 country code where the transaction occurred.                                                       |
| `lat`                                                                                                                     | *Optional[float]*                                                                                                         | :heavy_check_mark:                                                                                                        | The latitude where the transaction occurred.                                                                              |
| `lon`                                                                                                                     | *Optional[float]*                                                                                                         | :heavy_check_mark:                                                                                                        | The longitude where the transaction occurred.                                                                             |
| `postal_code`                                                                                                             | *Optional[str]*                                                                                                           | :heavy_check_mark:                                                                                                        | The postal code where the transaction occurred. In API versions 2018-05-22 and earlier, this field is called `zip`.       |
| `region`                                                                                                                  | *Optional[str]*                                                                                                           | :heavy_check_mark:                                                                                                        | The region or state where the transaction occurred. In API versions 2018-05-22 and earlier, this field is called `state`. |
| `store_number`                                                                                                            | *Optional[str]*                                                                                                           | :heavy_check_mark:                                                                                                        | The merchant defined store number where the transaction occurred.                                                         |