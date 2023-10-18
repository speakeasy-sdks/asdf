# EntityScreeningHitsPhoneNumberItems

Analyzed phone numbers for the associated hit


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                           | Dict[str, *Any*]                                                                                  | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `analysis`                                                                                        | [Optional[MatchSummary]](../../models/shared/matchsummary.md)                                     | :heavy_minus_sign:                                                                                | Summary object reflecting the match result of the associated data                                 |
| `data`                                                                                            | [Optional[EntityScreeningHitPhoneNumbers]](../../models/shared/entityscreeninghitphonenumbers.md) | :heavy_minus_sign:                                                                                | Phone number information associated with the entity screening hit                                 |