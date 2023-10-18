# IncomeVerificationPrecheckResponse

IncomeVerificationPrecheckResponse defines the response schema for `/income/verification/precheck`.


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                                                                                                                                                                                                           | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `confidence`                                                                                                                                                                                                                                                                                                                                                                                                                                      | [IncomeVerificationPrecheckConfidence](../../models/shared/incomeverificationprecheckconfidence.md)                                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                | The confidence that Plaid can support the user in the digital income verification flow instead of requiring a manual paystub upload. One of the following:<br/><br/>`"HIGH"`: It is very likely that this user can use the digital income verification flow.<br/><br/>"`LOW`": It is unlikely that this user can use the digital income verification flow.<br/><br/>`"UNKNOWN"`: It was not possible to determine if the user is supportable with the information passed. |
| `precheck_id`                                                                                                                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                | ID of the precheck. Provide this value when calling `/link/token/create` in order to optimize Link conversion.                                                                                                                                                                                                                                                                                                                                    |
| `request_id`                                                                                                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.                                                                                                                                                                                                                                                                                                       |