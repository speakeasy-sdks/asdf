# FDXNotificationPayload

Custom key-value pairs payload for a notification


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `custom_fields`                                                                               | list[[FDXFiAttribute](../../models/shared/fdxfiattribute.md)]                                 | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `id`                                                                                          | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | ID for the origination entity related to the notification                                     |
| `id_type`                                                                                     | [Optional[FDXNotificationPayloadIDType]](../../models/shared/fdxnotificationpayloadidtype.md) | :heavy_minus_sign:                                                                            | Type of entity causing origination of a notification                                          |