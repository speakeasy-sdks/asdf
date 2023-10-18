# AccountProductAccessNullable

Allow the application to access specific products on this account


## Fields

| Field                                                                                                                                     | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                   | Dict[str, *Any*]                                                                                                                          | :heavy_minus_sign:                                                                                                                        | N/A                                                                                                                                       |
| `account_data`                                                                                                                            | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Allow the application to access account data. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.    |
| `statements`                                                                                                                              | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Allow the application to access bank statements. Only used by certain partners. If relevant to the partner and unset, defaults to `true`. |
| `tax_documents`                                                                                                                           | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Allow the application to access tax documents. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.   |