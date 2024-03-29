"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditbankemploymentreport import CreditBankEmploymentReport
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankEmploymentGetResponse:
    r"""CreditBankEmploymentGetResponse defines the response schema for `/beta/credit/v1/bank_employment/get`."""
    UNSET='__SPEAKEASY_UNSET__'
    bank_employment_reports: List[CreditBankEmploymentReport] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_employment_reports') }})
    r"""Bank Employment data. Each entry in the array will be a distinct bank employment report."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

