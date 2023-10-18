# WalletTransactionCounterpartyNumbers

The counterparty's bank account numbers. Exactly one of IBAN or BACS data is required.


## Fields

| Field                                                                                                                     | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                   | Dict[str, *Any*]                                                                                                          | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `bacs`                                                                                                                    | [Optional[WalletTransactionCounterpartyBACS]](../../models/shared/wallettransactioncounterpartybacs.md)                   | :heavy_minus_sign:                                                                                                        | The account number and sort code of the counterparty's account                                                            |
| `international`                                                                                                           | [Optional[WalletTransactionCounterpartyInternational]](../../models/shared/wallettransactioncounterpartyinternational.md) | :heavy_minus_sign:                                                                                                        | International Bank Account Number for a Wallet Transaction                                                                |