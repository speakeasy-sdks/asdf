# TransactionsEnhanceGetResponse

TransactionsEnhanceGetResponse defines the response schema for `/beta/transactions/v1/enhance`.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `enhanced_transactions`                                                                                    | List[[shared.ClientProvidedEnhancedTransaction](../../models/shared/clientprovidedenhancedtransaction.md)] | :heavy_check_mark:                                                                                         | An array of enhanced transactions.                                                                         |
| `additional_properties`                                                                                    | Dict[str, *Any*]                                                                                           | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |