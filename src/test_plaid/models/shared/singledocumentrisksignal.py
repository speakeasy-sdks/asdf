"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import documentrisksignal as shared_documentrisksignal
from ..shared import documentrisksummary as shared_documentrisksummary
from ..shared import risksignaldocumentreference as shared_risksignaldocumentreference
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SingleDocumentRiskSignal:
    r"""Object containing all risk signals and relevant metadata for a single document"""
    document_reference: shared_risksignaldocumentreference.RiskSignalDocumentReference = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_reference') }})
    r"""Object containing metadata for the document"""
    risk_signals: List[shared_documentrisksignal.DocumentRiskSignal] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_signals') }})
    r"""Array of attributes that indicate whether or not there is fraud risk with a document"""
    risk_summary: shared_documentrisksummary.DocumentRiskSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_summary') }})
    r"""A summary across all risk signals associated with a document"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
