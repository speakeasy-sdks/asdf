# CreditBankIncomeSource

Detailed information for the income source.


## Fields

| Field                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | Plaid's unique identifier for the account.                                                                                                                                                                                                                                                                                             |
| `end_date`                                                                                                                                                                                                                                                                                                                             | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | Maximum of all dates within the specific income sources in the user’s bank account for days requested by the client.<br/>The date will be returned in an ISO 8601 format (YYYY-MM-DD).                                                                                                                                                 |
| `historical_summary`                                                                                                                                                                                                                                                                                                                   | List[[CreditBankIncomeHistoricalSummary](../../models/shared/creditbankincomehistoricalsummary.md)]                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                                                    |
| `income_category`                                                                                                                                                                                                                                                                                                                      | [Optional[CreditBankIncomeCategory]](../../models/shared/creditbankincomecategory.md)                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | The income category. Note that the `CASH` value has been deprecated and is used only for existing legacy implementations. It has been replaced by the new categories `CASH_DEPOSIT` (representing cash or check deposits) and `TRANSFER_FROM_APPLICATION` (representing cash transfers originating from apps, such as Zelle or Venmo). |
| `income_description`                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | The most common name or original description for the underlying income transactions.                                                                                                                                                                                                                                                   |
| `income_source_id`                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | A unique identifier for an income source.                                                                                                                                                                                                                                                                                              |
| `pay_frequency`                                                                                                                                                                                                                                                                                                                        | [Optional[CreditBankIncomePayFrequency]](../../models/shared/creditbankincomepayfrequency.md)                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | The income pay frequency.                                                                                                                                                                                                                                                                                                              |
| `start_date`                                                                                                                                                                                                                                                                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | Minimum of all dates within the specific income sources in the user's bank account for days requested by the client.<br/>The date will be returned in an ISO 8601 format (YYYY-MM-DD).                                                                                                                                                 |
| `total_amount`                                                                                                                                                                                                                                                                                                                         | *Optional[float]*                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | Total amount of earnings in the user’s bank account for the specific income source for days requested by the client.                                                                                                                                                                                                                   |
| `transaction_count`                                                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                     | Number of transactions for the income source within the start and end date.                                                                                                                                                                                                                                                            |