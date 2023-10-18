# PSLFStatus

Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is FedLoan (`ins_116527`). 


## Fields

| Field                                                                                                                                                             | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                           | Dict[str, *Any*]                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `estimated_eligibility_date`                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                      | :heavy_check_mark:                                                                                                                                                | The estimated date borrower will have completed 120 qualifying monthly payments. Returned in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `payments_made`                                                                                                                                                   | *Optional[int]*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                | The number of qualifying payments that have been made.                                                                                                            |
| `payments_remaining`                                                                                                                                              | *Optional[int]*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                | The number of qualifying payments remaining.                                                                                                                      |