# MultiDocumentRiskSignal

Object containing risk signals and relevant metadata for a set of uploaded documents


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `document_references`                                                                          | List[[shared.RiskSignalDocumentReference](../../models/shared/risksignaldocumentreference.md)] | :heavy_check_mark:                                                                             | Array of objects containing attributes that could indicate if a document is fraudulent         |
| `risk_signals`                                                                                 | List[[shared.DocumentRiskSignal](../../models/shared/documentrisksignal.md)]                   | :heavy_check_mark:                                                                             | Array of attributes that indicate whether or not there is fraud risk with a set of documents   |
| `additional_properties`                                                                        | Dict[str, *Any*]                                                                               | :heavy_minus_sign:                                                                             | N/A                                                                                            |