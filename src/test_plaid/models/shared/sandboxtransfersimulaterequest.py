"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SandboxTransferSimulateRequest:
    r"""Defines the request schema for `/sandbox/transfer/simulate`"""
    event_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_type') }})
    r"""The asynchronous event to be simulated. May be: `posted`, `settled`, `failed`, or `returned`.

    An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:

    `pending` --> `failed`

    `pending` --> `posted`

    `posted` --> `returned`

    `posted` --> `settled`
    """
    transfer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transfer_id') }})
    r"""Plaid’s unique identifier for a transfer."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    failure_reason: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failure_reason') }})
    r"""The failure reason if the event type for a transfer is `\\"failed\\"` or `\\"returned\\"`. Null value otherwise."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    test_clock_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test_clock_id') }})
    r"""Plaid’s unique identifier for a test clock. If provided, the event to be simulated is created at the `virtual_time` on the provided `test_clock`."""
    

