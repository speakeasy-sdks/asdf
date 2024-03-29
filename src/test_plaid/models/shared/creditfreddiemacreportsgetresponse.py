"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfreddiemacverificationofassets_voa_2_4 import CreditFreddieMacVerificationOfAssetsVOA24
from .creditfreddieverificationofemployment_voe_2_5 import CreditFreddieVerificationOfEmploymentVOE25
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacReportsGetResponse:
    r"""CreditFreddieMacReportsGetResponse defines the response schema for `/credit/freddie_mac/reports/get`"""
    UNSET='__SPEAKEASY_UNSET__'
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    voa: Optional[CreditFreddieMacVerificationOfAssetsVOA24] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VOA'), 'exclude': lambda f: f is CreditFreddieMacReportsGetResponse.UNSET }})
    r"""Verification of Assets Report"""
    voe: Optional[CreditFreddieVerificationOfEmploymentVOE25] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VOE'), 'exclude': lambda f: f is CreditFreddieMacReportsGetResponse.UNSET }})
    r"""Verification of Employment Report"""
    

