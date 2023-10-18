# BankTransferUser

The legal name and other information for the account holder.


## Fields

| Field                                                                                                                               | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                             | Dict[str, *Any*]                                                                                                                    | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `email_address`                                                                                                                     | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | The account holder’s email.                                                                                                         |
| `legal_name`                                                                                                                        | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The account holder’s full legal name. If the transfer `ach_class` is `ccd`, this should be the business name of the account holder. |
| `routing_number`                                                                                                                    | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | The account holder's routing number. This field is only used in response data. Do not provide this field when making requests.      |