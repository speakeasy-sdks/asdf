# BankTransferFailure

The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise.


## Fields

| Field                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                 | Dict[str, *Any*]                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                     |
| `ach_return_code`                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | The ACH return code, e.g. `R01`.  A return code will be provided if and only if the transfer status is `reversed`. For a full listing of ACH return codes, see [Bank Transfers errors](https://plaid.com/docs/errors/bank-transfers/#ach-return-codes). |
| `description`                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                      | A human-readable description of the reason for the failure or reversal.                                                                                                                                                                                 |