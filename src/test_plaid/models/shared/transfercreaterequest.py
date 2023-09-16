"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import transferuserinrequestdeprecated as shared_transferuserinrequestdeprecated
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from test_plaid import utils
from typing import Optional

class TransferCreateRequestACHClass(str, Enum):
    r"""Specifies the use case of the transfer. Required for transfers on an ACH network.

    `\"ccd\"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    `\"ppd\"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment

    `\"tel\"` - Telephone-Initiated Entry

    `\"web\"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    CCD = 'ccd'
    PPD = 'ppd'
    TEL = 'tel'
    WEB = 'web'

class TransferCreateRequestTransferNetwork(str, Enum):
    r"""The network or rails used for the transfer.

    For transfers submitted as either `ach` or `same-day-ach` the cutoff for same-day is 3:30 PM Eastern Time and the cutoff for next-day transfers is 5:30 PM Eastern Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    ACH = 'ach'
    SAME_DAY_ACH = 'same-day-ach'
    RTP = 'rtp'

class TransferCreateRequestTransferType(str, Enum):
    r"""The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    DEBIT = 'debit'
    CREDIT = 'credit'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TransferCreateRequest:
    r"""Defines the request schema for `/transfer/create`"""
    authorization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization_id') }})
    r"""Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier."""
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""The transfer description. Maximum of 15 characters. If reprocessing a returned transfer, please note that the `description` field must be `\\"Retry\\"` to indicate that it's a retry of a previously returned transfer. You may retry a transfer up to 2 times, within 180 days of creating the original transfer. Only transfers that were returned with code `R01` or `R09` may be retried. For a full listing of ACH return codes, see [Transfer errors](https://plaid.com/docs/errors/transfer/#ach-return-codes)."""
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""The Plaid `access_token` for the account that will be debited or credited. Required if not using `payment_profile_token`."""
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id'), 'exclude': lambda f: f is None }})
    r"""The Plaid `account_id` corresponding to the end-user account that will be debited or credited. Required when creating a transfer using an `access_token`."""
    ach_class: Optional[TransferCreateRequestACHClass] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ach_class'), 'exclude': lambda f: f is None }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""The amount of the transfer (decimal string with two digits of precision e.g. \\"10.00\\")."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('idempotency_key'), 'exclude': lambda f: f is None }})
    r"""Deprecated. `authorization_id` is now used as idempotency instead.

    A random key provided by the client, per unique transfer. Maximum of 50 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single transfer is created.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    iso_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code'), 'exclude': lambda f: f is None }})
    r"""The currency of the transfer amount. The default value is \\"USD\\".

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    metadata: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    The JSON values must be Strings (no nested JSON objects allowed)
    Only ASCII characters may be used
    Maximum of 50 key/value pairs
    Maximum key length of 40 characters
    Maximum value length of 500 characters
    """
    network: Optional[TransferCreateRequestTransferNetwork] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network'), 'exclude': lambda f: f is None }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    origination_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_account_id'), 'exclude': lambda f: f is None }})
    r"""Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    payment_profile_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_profile_token'), 'exclude': lambda f: f is None }})
    r"""The payment profile token associated with the Payment Profile that will be debited or credited. Required if not using `access_token`."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    test_clock_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test_clock_id'), 'exclude': lambda f: f is None }})
    r"""Plaid’s unique identifier for a test clock. This field may only be used when using `sandbox` environment. If provided, the `transfer` is created at the `virtual_time` on the provided `test_clock`."""
    type: Optional[TransferCreateRequestTransferType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    user: Optional[shared_transferuserinrequestdeprecated.TransferUserInRequestDeprecated] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""The legal name and other information for the account holder.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    

