"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .wallet import Wallet
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletListResponse:
    r"""WalletListResponse defines the response schema for `/wallet/list`"""
    UNSET='__SPEAKEASY_UNSET__'
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    wallets: List[Wallet] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallets') }})
    r"""An array of e-wallets"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    next_cursor: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_cursor'), 'exclude': lambda f: f is None }})
    r"""Cursor used for fetching e-wallets created before the latest e-wallet provided in this response"""
    

