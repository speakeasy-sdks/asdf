# SelfieCheckSelfie

Captures and analysis from a user's selfie.


## Fields

| Field                                                                                                                                                                                     | Type                                                                                                                                                                                      | Required                                                                                                                                                                                  | Description                                                                                                                                                                               | Example                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                   | Dict[str, *Any*]                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                        | N/A                                                                                                                                                                                       |                                                                                                                                                                                           |
| `analysis`                                                                                                                                                                                | [SelfieAnalysis](../../models/shared/selfieanalysis.md)                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                        | High level descriptions of how the associated selfie was processed. If a selfie fails verification, the details in the `analysis` object should help clarify why the selfie was rejected. |                                                                                                                                                                                           |
| `attempt`                                                                                                                                                                                 | *int*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | The `attempt` field begins with 1 and increments with each subsequent selfie upload.                                                                                                      | 1                                                                                                                                                                                         |
| `capture`                                                                                                                                                                                 | [SelfieCapture](../../models/shared/selfiecapture.md)                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | The image or video capture of a selfie. Only one of image or video URL will be populated per selfie.                                                                                      |                                                                                                                                                                                           |
| `status`                                                                                                                                                                                  | [SelfieStatus](../../models/shared/selfiestatus.md)                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                        | An outcome status for this specific selfie. Distinct from the overall `selfie_check.status` that summarizes the verification outcome from one or more selfies.                            | success                                                                                                                                                                                   |