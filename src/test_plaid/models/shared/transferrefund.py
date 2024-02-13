"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .transferrefundfailure import TransferRefundFailure
from .transferrefundstatus import TransferRefundStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferRefund:
    r"""Represents a refund within the Transfers API."""
    UNSET='__SPEAKEASY_UNSET__'
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount of the refund (decimal string with two digits of precision e.g. \\"10.00\\")."""
    created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The datetime when this refund was created. This will be of the form `2006-01-02T15:04:05Z`"""
    failure_reason: Optional[TransferRefundFailure] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failure_reason') }})
    r"""The failure reason if the event type for a refund is `\\"failed\\"` or `\\"returned\\"`. Null value otherwise."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Plaid’s unique identifier for a refund."""
    status: TransferRefundStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the refund.

    `pending`: A new refund was created; it is in the pending state.
    `posted`: The refund has been successfully submitted to the payment network.
    `settled`: Credits have been refunded to the Plaid linked account.
    `cancelled`: The refund was cancelled by the client.
    `failed`: The refund has failed.
    `returned`: The refund was returned.
    """
    transfer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transfer_id') }})
    r"""The ID of the transfer to refund."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

