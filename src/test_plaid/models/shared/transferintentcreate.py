"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .achclass import ACHClass
from .transferintentcreatemode import TransferIntentCreateMode
from .transferintentcreatenetwork import TransferIntentCreateNetwork
from .transferintentstatus import TransferIntentStatus
from .transferuserinresponse import TransferUserInResponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferIntentCreate:
    r"""Represents a transfer intent within Transfer UI."""
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount of the transfer (decimal string with two digits of precision e.g. \\"10.00\\")."""
    created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The datetime the transfer was created. This will be of the form `2006-01-02T15:04:05Z`."""
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""A description for the underlying transfer. Maximum of 8 characters."""
    funding_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('funding_account_id') }})
    r"""The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Plaid's unique identifier for the transfer intent object."""
    iso_currency_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The currency of the transfer amount, e.g. \\"USD\\" """
    mode: TransferIntentCreateMode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    r"""The direction of the flow of transfer funds.

    `PAYMENT`: Transfers funds from an end user's account to your business account.

    `DISBURSEMENT`: Transfers funds from your business account to an end user's account.
    """
    origination_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_account_id') }})
    r"""Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    status: TransferIntentStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the transfer intent.

    `PENDING`: The transfer intent is pending.
    `SUCCEEDED`: The transfer intent was successfully created.
    `FAILED`: The transfer intent was unable to be created.
    """
    user: TransferUserInResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""The legal name and other information for the account holder."""
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The Plaid `account_id` corresponding to the end-user account that will be debited or credited. Returned only if `account_id` was set on intent creation."""
    ach_class: Optional[ACHClass] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ach_class'), 'exclude': lambda f: f is None }})
    r"""Specifies the use case of the transfer. Required for transfers on an ACH network.

    `\"ccd\"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    `\"ppd\"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment

    `\"tel\"` - Telephone-Initiated Entry

    `\"web\"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    metadata: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    The JSON values must be Strings (no nested JSON objects allowed)
    Only ASCII characters may be used
    Maximum of 50 key/value pairs
    Maximum key length of 40 characters
    Maximum value length of 500 characters
    """
    network: Optional[TransferIntentCreateNetwork] = dataclasses.field(default=TransferIntentCreateNetwork.SAME_DAY_ACH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network'), 'exclude': lambda f: f is None }})
    r"""The network or rails used for the transfer. Defaults to `same-day-ach`.

    For transfers submitted as either `ach` or `same-day-ach` the cutoff for same-day is 3:30 PM Eastern Time and the cutoff for next-day transfers is 5:30 PM Eastern Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable.
    """
    require_guarantee: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('require_guarantee') }})
    r"""When `true`, the transfer requires a `GUARANTEED` decision by Plaid to proceed (Guarantee customers only)."""
    

