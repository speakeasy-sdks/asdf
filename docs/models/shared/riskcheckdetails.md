# RiskCheckDetails

Additional information for the `risk_check` step.


## Fields

| Field                                                                                                                | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                              | Dict[str, *Any*]                                                                                                     | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |                                                                                                                      |
| `behavior`                                                                                                           | [Optional[RiskCheckBehavior]](../../models/shared/riskcheckbehavior.md)                                              | :heavy_check_mark:                                                                                                   | Result summary object specifying values for `behavior` attributes of risk check, when available.                     |                                                                                                                      |
| `devices`                                                                                                            | List[[RiskCheckDevice](../../models/shared/riskcheckdevice.md)]                                                      | :heavy_check_mark:                                                                                                   | Array of result summary objects specifying values for `device` attributes of risk check.                             |                                                                                                                      |
| `email`                                                                                                              | [Optional[RiskCheckEmail]](../../models/shared/riskcheckemail.md)                                                    | :heavy_check_mark:                                                                                                   | Result summary object specifying values for `email` attributes of risk check.                                        |                                                                                                                      |
| `identity_abuse_signals`                                                                                             | [Optional[RiskCheckIdentityAbuseSignals]](../../models/shared/riskcheckidentityabusesignals.md)                      | :heavy_check_mark:                                                                                                   | Result summary object capturing abuse signals related to `identity abuse`, e.g. stolen and synthetic identity fraud. |                                                                                                                      |
| `phone`                                                                                                              | [Optional[RiskCheckPhone]](../../models/shared/riskcheckphone.md)                                                    | :heavy_check_mark:                                                                                                   | Result summary object specifying values for `phone` attributes of risk check.                                        |                                                                                                                      |
| `status`                                                                                                             | [IdentityVerificationStepStatus](../../models/shared/identityverificationstepstatus.md)                              | :heavy_check_mark:                                                                                                   | The status of a step in the identity verification process.                                                           | success                                                                                                              |