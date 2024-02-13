"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DepositSwitchAltCreateResponse:
    r"""DepositSwitchAltCreateResponse defines the response schema for `/deposit_switch/alt/create`"""
    UNSET='__SPEAKEASY_UNSET__'
    deposit_switch_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deposit_switch_id') }})
    r"""ID of the deposit switch. This ID is persisted throughout the lifetime of the deposit switch."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

