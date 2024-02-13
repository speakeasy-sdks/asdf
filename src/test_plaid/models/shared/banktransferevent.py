"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .banktransferdirection import BankTransferDirection
from .banktransfereventtype import BankTransferEventType
from .banktransferfailure import BankTransferFailure
from .banktransfertype import BankTransferType
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BankTransferEvent:
    r"""Represents an event in the Bank Transfers API."""
    UNSET='__SPEAKEASY_UNSET__'
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The account ID associated with the bank transfer."""
    bank_transfer_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_transfer_amount') }})
    r"""The bank transfer amount."""
    bank_transfer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_transfer_id') }})
    r"""Plaid’s unique identifier for a bank transfer."""
    bank_transfer_iso_currency_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_transfer_iso_currency_code') }})
    r"""The currency of the bank transfer amount."""
    bank_transfer_type: BankTransferType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_transfer_type') }})
    r"""The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""
    direction: Optional[BankTransferDirection] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('direction') }})
    r"""Indicates the direction of the transfer: `outbound` for API-initiated transfers, or `inbound` for payments received by the FBO account."""
    event_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_id') }})
    r"""Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers."""
    event_type: BankTransferEventType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event_type') }})
    r"""The type of event that this bank transfer represents.

    `pending`: A new transfer was created; it is in the pending state.

    `cancelled`: The transfer was cancelled by the client.

    `failed`: The transfer failed, no funds were moved.

    `posted`: The transfer has been successfully submitted to the payment network.

    `reversed`: A posted transfer was reversed.
    """
    failure_reason: Optional[BankTransferFailure] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failure_reason') }})
    r"""The failure reason if the type of this transfer is `\\"failed\\"` or `\\"reversed\\"`. Null value otherwise."""
    origination_account_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_account_id') }})
    r"""The ID of the origination account that this balance belongs to."""
    timestamp: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

