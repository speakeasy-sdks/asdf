# TransactionsRuleDetails

A representation of transactions rule details.


## Fields

| Field                                                                                                           | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `field`                                                                                                         | [TransactionsRuleField](../../models/shared/transactionsrulefield.md)                                           | :heavy_check_mark:                                                                                              | Transaction field for which the rule is defined.                                                                |
| `query`                                                                                                         | *str*                                                                                                           | :heavy_check_mark:                                                                                              | For TRANSACTION_ID field, provide transaction_id. For NAME field, provide a string pattern.<br/>                |
| `type`                                                                                                          | [TransactionsRuleType](../../models/shared/transactionsruletype.md)                                             | :heavy_check_mark:                                                                                              | Transaction rule's match type. For TRANSACTION_ID field, EXACT_MATCH is available.<br/>Matches are case sensitive.<br/> |