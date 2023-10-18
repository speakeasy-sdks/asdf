"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import achclass as shared_achclass
from ..shared import transfernetwork as shared_transfernetwork
from ..shared import transferrecurringschedule as shared_transferrecurringschedule
from ..shared import transferrecurringstatus as shared_transferrecurringstatus
from ..shared import transfertype as shared_transfertype
from ..shared import transferuserinresponse as shared_transferuserinresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RecurringTransferNullable:
    r"""Represents a recurring transfer within the Transfers API."""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The Plaid `account_id` corresponding to the end-user account that will be debited or credited."""
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount of the transfer (decimal string with two digits of precision e.g. \\"10.00\\")."""
    created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`"""
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""The description of the recurring transfer."""
    funding_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('funding_account_id') }})
    r"""The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited."""
    iso_currency_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The currency of the transfer amount, e.g. \\"USD\\" """
    network: shared_transfernetwork.TransferNetwork = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network') }})
    r"""The network or rails used for the transfer.

    For transfers submitted as either `ach` or `same-day-ach` the cutoff for same-day is 3:30 PM Eastern Time and the cutoff for next-day transfers is 5:30 PM Eastern Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable.
    """
    next_origination_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_origination_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).

    The next transfer origination date after bank holiday adjustment.
    """
    origination_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_account_id') }})
    r"""Plaid’s unique identifier for the origination account that was used for this transfer.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    recurring_transfer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recurring_transfer_id') }})
    r"""Plaid’s unique identifier for a recurring transfer."""
    schedule: shared_transferrecurringschedule.TransferRecurringSchedule = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
    r"""The schedule that the recurring transfer will be executed on."""
    status: shared_transferrecurringstatus.TransferRecurringStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the recurring transfer.

    `active`: The recurring transfer is currently active.
    `cancelled`: The recurring transfer was cancelled by the client or Plaid.
    `expired`: The recurring transfer has completed all originations according to its recurring schedule.
    """
    transfer_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transfer_ids') }})
    type: shared_transfertype.TransferType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""
    user: shared_transferuserinresponse.TransferUserInResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""The legal name and other information for the account holder."""
    ach_class: Optional[shared_achclass.ACHClass] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ach_class'), 'exclude': lambda f: f is None }})
    r"""Specifies the use case of the transfer. Required for transfers on an ACH network.

    `\"ccd\"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    `\"ppd\"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment

    `\"tel\"` - Telephone-Initiated Entry

    `\"web\"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    test_clock_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test_clock_id') }})
    r"""Plaid’s unique identifier for a test clock."""
    

