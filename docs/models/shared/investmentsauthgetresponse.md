# InvestmentsAuthGetResponse

InvestmentsAuthGetResponse defines the response schema for `/investments/auth/get`


## Fields

| Field                                                                                                                                                      | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                    | Dict[str, *Any*]                                                                                                                                           | :heavy_minus_sign:                                                                                                                                         | N/A                                                                                                                                                        |
| `accounts`                                                                                                                                                 | List[[AccountBase](../../models/shared/accountbase.md)]                                                                                                    | :heavy_check_mark:                                                                                                                                         | The accounts for which data is being retrieved                                                                                                             |
| `holdings`                                                                                                                                                 | List[[Holding](../../models/shared/holding.md)]                                                                                                            | :heavy_check_mark:                                                                                                                                         | The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the `securities` field.  |
| `item`                                                                                                                                                     | [Item](../../models/shared/item.md)                                                                                                                        | :heavy_check_mark:                                                                                                                                         | Metadata about the Item.                                                                                                                                   |
| `numbers`                                                                                                                                                  | [InvestmentsAuthGetNumbers](../../models/shared/investmentsauthgetnumbers.md)                                                                              | :heavy_check_mark:                                                                                                                                         | Identifying information for transferring holdings to an investments account.                                                                               |
| `owners`                                                                                                                                                   | List[[InvestmentsAuthOwner](../../models/shared/investmentsauthowner.md)]                                                                                  | :heavy_check_mark:                                                                                                                                         | Information about the account owners for the accounts associated with the Item.                                                                            |
| `request_id`                                                                                                                                               | *str*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.                |
| `securities`                                                                                                                                               | List[[Security](../../models/shared/security.md)]                                                                                                          | :heavy_check_mark:                                                                                                                                         | Objects describing the securities held in the accounts associated with the Item.                                                                           |