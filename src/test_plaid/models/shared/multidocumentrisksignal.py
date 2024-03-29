"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .documentrisksignal import DocumentRiskSignal
from .risksignaldocumentreference import RiskSignalDocumentReference
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MultiDocumentRiskSignal:
    r"""Object containing risk signals and relevant metadata for a set of uploaded documents"""
    UNSET='__SPEAKEASY_UNSET__'
    document_references: List[RiskSignalDocumentReference] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_references') }})
    r"""Array of objects containing attributes that could indicate if a document is fraudulent"""
    risk_signals: List[DocumentRiskSignal] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_signals') }})
    r"""Array of attributes that indicate whether or not there is fraud risk with a set of documents"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

