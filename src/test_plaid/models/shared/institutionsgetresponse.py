"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .institution import Institution
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InstitutionsGetResponse:
    r"""InstitutionsGetResponse defines the response schema for `/institutions/get`"""
    UNSET='__SPEAKEASY_UNSET__'
    institutions: List[Institution] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institutions') }})
    r"""A list of Plaid institutions"""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    total: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    r"""The total number of institutions available via this endpoint"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

