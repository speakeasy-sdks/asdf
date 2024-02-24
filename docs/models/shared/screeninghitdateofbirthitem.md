# ScreeningHitDateOfBirthItem

Analyzed date of birth for the associated hit


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `additional_properties`                                              | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `analysis`                                                           | [Optional[shared.MatchSummary]](../../models/shared/matchsummary.md) | :heavy_minus_sign:                                                   | Summary object reflecting the match result of the associated data    |                                                                      |
| `data`                                                               | [Optional[shared.DateRange]](../../models/shared/daterange.md)       | :heavy_minus_sign:                                                   | A date range with a start and end date                               | {<br/>"ending": "1966-06-30",<br/>"beginning": "1966-06-01"<br/>}    |