# FDXNotificationPayload

Custom key-value pairs payload for a notification


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `custom_fields`                                                                                      | List[[shared.FDXFiAttribute](../../models/shared/fdxfiattribute.md)]                                 | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `id`                                                                                                 | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | ID for the origination entity related to the notification                                            |
| `id_type`                                                                                            | [Optional[shared.FDXNotificationPayloadIDType]](../../models/shared/fdxnotificationpayloadidtype.md) | :heavy_minus_sign:                                                                                   | Type of entity causing origination of a notification                                                 |