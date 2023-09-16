# PaymentInitiationConsentConstraints

Limitations that will be applied to payments initiated using the payment consent.


## Fields

| Field                                                                                                                                | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `max_payment_amount`                                                                                                                 | [PaymentAmount](../../models/shared/paymentamount.md)                                                                                | :heavy_check_mark:                                                                                                                   | Maximum amount of a single payment initiated using the payment consent.                                                              |
| `periodic_amounts`                                                                                                                   | list[[PaymentConsentPeriodicAmount](../../models/shared/paymentconsentperiodicamount.md)]                                            | :heavy_check_mark:                                                                                                                   | A list of amount limitations per period of time.                                                                                     |
| `valid_date_time`                                                                                                                    | [Optional[PaymentConsentValidDateTime]](../../models/shared/paymentconsentvaliddatetime.md)                                          | :heavy_minus_sign:                                                                                                                   | Life span for the payment consent. After the `to` date the payment consent expires and can no longer be used for payment initiation. |