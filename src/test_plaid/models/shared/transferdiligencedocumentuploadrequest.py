"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import transferdocumentpurpose as shared_transferdocumentpurpose
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TransferDiligenceDocumentUploadRequest:
    r"""Defines the request schema for `/transfer/diligence/document/upload`"""
    file: bytes = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file') }})
    r"""A file to upload."""
    originator_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('originator_client_id') }})
    r"""The Client ID of the originator whose document that you want to upload."""
    purpose: shared_transferdocumentpurpose.TransferDocumentPurpose = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purpose') }})
    r"""Specifies the purpose of the uploaded file.

    `\"DUE_DILIGENCE\"` - The transfer due diligence document of the originator.
    The size of the document should be less than 20MB. Supported file extension: .pdf, .docx, .doc.
    """
    

