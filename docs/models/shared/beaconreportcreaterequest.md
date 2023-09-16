# BeaconReportCreateRequest

Request input for creating a Beacon Report


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `beacon_user_id`                                                                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                | ID of the associated Beacon User.                                                                                                                                                                                                                                                                                                                                                                 | becusr_11111111111111                                                                                                                                                                                                                                                                                                                                                                             |
| `client_id`                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                   |
| `fraud_amount`                                                                                                                                                                                                                                                                                                                                                                                    | dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | The amount and currency of the fraud or attempted fraud.<br/>`fraud_amount` should be omitted to indicate an unknown fraud amount.                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                   |
| `fraud_date`                                                                                                                                                                                                                                                                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).                                                                                                                                                                                                                                                                                                                                           | 1990-05-29                                                                                                                                                                                                                                                                                                                                                                                        |
| `secret`                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                   |
| `type`                                                                                                                                                                                                                                                                                                                                                                                            | [BeaconReportType](../../models/shared/beaconreporttype.md)                                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                | The type of Beacon Report.<br/><br/>`first_party`: If this is the same individual as the one who submitted the KYC.<br/><br/>`third_party`: If this is a different individual from the one who submitted the KYC.<br/><br/>`synthetic`: If this is an individual using fabricated information.<br/><br/>`account_takeover`: If this individual's account was compromised.<br/><br/>`unknown`: If you aren't sure who committed the fraud. |                                                                                                                                                                                                                                                                                                                                                                                                   |