# Holding

A securities holding at an institution.


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `account_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The Plaid `account_id` associated with the holding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `cost_basis`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The original total value of the holding. This field is calculated by Plaid as the sum of the purchase price of all of the shares in the holding.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `institution_price`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *float*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The last price given by the institution for this security.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `institution_price_as_of`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The date at which `institution_price` was current.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `institution_price_datetime`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Date and time at which `institution_price` was current, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ).<br/><br/>This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00).<br/>                                                                                                                                                                                                                                                                                              |
| `institution_value`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *float*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The value of the holding, as reported by the institution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `iso_currency_code`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The ISO-4217 currency code of the holding. Always `null` if `unofficial_currency_code` is non-`null`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `quantity`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The total quantity of the asset held, as reported by the financial institution. If the security is an option, `quantity` will reflect the total number of options (typically the number of contracts multiplied by 100), not the number of contracts.                                                                                                                                                                                                                                                                                                                   |
| `security_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The Plaid `security_id` associated with the holding. Security data is not specific to a user's account; any user who held the same security at the same financial institution at the same time would have identical security data. The `security_id` for the same security will typically be the same across different institutions, but this is not guaranteed. The `security_id` does not typically change, but may change if inherent details of the security change due to a corporate action, for example, in the event of a ticker symbol change or CUSIP change. |
| `unofficial_currency_code`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.<br/><br/>See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.<br/>                                                                                                                            |