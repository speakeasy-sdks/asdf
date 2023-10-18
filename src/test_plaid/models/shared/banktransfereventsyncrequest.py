"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BankTransferEventSyncRequest:
    r"""Defines the request schema for `/bank_transfer/event/sync`"""
    after_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('after_id') }})
    r"""The latest (largest) `event_id` fetched via the sync endpoint, or 0 initially."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    count: Optional[int] = dataclasses.field(default=25, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    r"""The maximum number of bank transfer events to return."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

