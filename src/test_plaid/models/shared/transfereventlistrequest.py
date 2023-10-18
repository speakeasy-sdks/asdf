"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import transfereventlisttransfertype as shared_transfereventlisttransfertype
from ..shared import transfereventtype as shared_transfereventtype
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferEventListRequest:
    r"""Defines the request schema for `/transfer/event/list`"""
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The account ID to get events for all transactions to/from an account."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    count: Optional[int] = dataclasses.field(default=25, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    r"""The maximum number of transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned."""
    end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse }})
    r"""The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)"""
    event_types: Optional[List[shared_transfereventtype.TransferEventType]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_types'), 'exclude': lambda f: f is None }})
    r"""Filter events by event type."""
    funding_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('funding_account_id') }})
    r"""Filter transfer events to only those with the specified `funding_account_id`."""
    offset: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offset') }})
    r"""The offset into the list of transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 events will be returned."""
    origination_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_account_id') }})
    r"""The origination account ID to get events for transfers from a specific origination account.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    originator_client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('originator_client_id') }})
    r"""Filter transfer events to only those with the specified originator client."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse }})
    r"""The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)"""
    sweep_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sweep_id'), 'exclude': lambda f: f is None }})
    r"""Plaid’s unique identifier for a sweep."""
    transfer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transfer_id') }})
    r"""Plaid’s unique identifier for a transfer."""
    transfer_type: Optional[shared_transfereventlisttransfertype.TransferEventListTransferType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transfer_type') }})
    r"""The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into your origination account; a `credit` indicates a transfer of money out of your origination account."""
    

