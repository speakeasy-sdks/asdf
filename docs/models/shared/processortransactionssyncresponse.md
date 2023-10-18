# ProcessorTransactionsSyncResponse

ProcessorTransactionsSyncResponse defines the response schema for `/processor/transactions/sync`


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                                                                                                              | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                                                                  |
| `added`                                                                                                                                                                                                                                                                                                                                              | List[[Transaction](../../models/shared/transaction.md)]                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                   | Transactions that have been added to the Item since `cursor` ordered by ascending last modified time.                                                                                                                                                                                                                                                |
| `has_more`                                                                                                                                                                                                                                                                                                                                           | *bool*                                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                   | Represents if more than requested count of transaction updates exist. If true, the additional updates can be fetched by making an additional request with `cursor` set to `next_cursor`. If `has_more` is true, it’s important to pull all available pages, to make it less likely for underlying data changes to conflict with pagination.          |
| `modified`                                                                                                                                                                                                                                                                                                                                           | List[[Transaction](../../models/shared/transaction.md)]                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                   | Transactions that have been modified on the Item since `cursor` ordered by ascending last modified time.                                                                                                                                                                                                                                             |
| `next_cursor`                                                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                   | Cursor used for fetching any future updates after the latest update provided in this response. The cursor obtained after all pages have been pulled (indicated by `has_more` being `false`) will be valid for at least 1 year. This cursor should be persisted for later calls. If transactions are not yet available, this will be an empty string. |
| `removed`                                                                                                                                                                                                                                                                                                                                            | List[[RemovedTransaction](../../models/shared/removedtransaction.md)]                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                   | Transactions that have been removed from the Item since `cursor` ordered by ascending last modified time.                                                                                                                                                                                                                                            |
| `request_id`                                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                   | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.                                                                                                                                                                                                          |