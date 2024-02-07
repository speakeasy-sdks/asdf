# SingleDocumentRiskSignal

Object containing all risk signals and relevant metadata for a single document


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `document_reference`                                                                     | [shared.RiskSignalDocumentReference](../../models/shared/risksignaldocumentreference.md) | :heavy_check_mark:                                                                       | Object containing metadata for the document                                              |
| `risk_signals`                                                                           | List[[shared.DocumentRiskSignal](../../models/shared/documentrisksignal.md)]             | :heavy_check_mark:                                                                       | Array of attributes that indicate whether or not there is fraud risk with a document     |
| `risk_summary`                                                                           | [shared.DocumentRiskSummary](../../models/shared/documentrisksummary.md)                 | :heavy_check_mark:                                                                       | A summary across all risk signals associated with a document                             |
| `additional_properties`                                                                  | Dict[str, *Any*]                                                                         | :heavy_minus_sign:                                                                       | N/A                                                                                      |