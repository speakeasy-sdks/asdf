# RiskSignalDocumentReference

Object containing metadata for the document


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                      | Dict[str, *Any*]                                                                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `document_id`                                                                                | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | An identifier of the document referenced by the document metadata.                           |
| `document_name`                                                                              | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | The name of the document                                                                     |
| `status`                                                                                     | [Optional[shared.RiskSignalDocumentStatus]](../../models/shared/risksignaldocumentstatus.md) | :heavy_minus_sign:                                                                           | Status of a document for risk signal analysis                                                |