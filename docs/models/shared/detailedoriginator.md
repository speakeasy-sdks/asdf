# DetailedOriginator

Originator and their status.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `client_id`                                                                      | *str*                                                                            | :heavy_check_mark:                                                               | Originator’s client ID.                                                          |
| `company_name`                                                                   | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `transfer_diligence_status`                                                      | [shared.TransferDiligenceStatus](../../models/shared/transferdiligencestatus.md) | :heavy_check_mark:                                                               | Originator’s diligence status.                                                   |
| `additional_properties`                                                          | Dict[str, *Any*]                                                                 | :heavy_minus_sign:                                                               | N/A                                                                              |