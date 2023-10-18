# CreditPayrollIncomeRefreshResponse

CreditPayrollIncomeRefreshResponse defines the response schema for `/credit/payroll_income/refresh`


## Fields

| Field                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                                                   | Dict[str, *Any*]                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                        | N/A                                                                                                                                                                                                                                                                                       |
| `request_id`                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                        | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.                                                                                                                                               |
| `verification_refresh_status`                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                        | The verification refresh status. One of the following:<br/><br/>`"USER_PRESENCE_REQUIRED"` User presence is required to refresh an income verification.<br/>`"SUCCESSFUL"` The income verification refresh was successful.<br/>`"NOT_FOUND"` No new data was found after the income verification refresh. |