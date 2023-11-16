"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .recurringtransfer import RecurringTransfer
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferRecurringGetResponse:
    r"""Defines the response schema for `/transfer/recurring/get`"""
    recurring_transfer: RecurringTransfer = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recurring_transfer') }})
    r"""Represents a recurring transfer within the Transfers API."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

