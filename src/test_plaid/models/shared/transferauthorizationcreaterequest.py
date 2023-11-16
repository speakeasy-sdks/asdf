"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .achclass import ACHClass
from .transferauthorizationdevice import TransferAuthorizationDevice
from .transferauthorizationuserinrequest import TransferAuthorizationUserInRequest
from .transfercreditfundssource import TransferCreditFundsSource
from .transfernetwork import TransferNetwork
from .transfertype import TransferType
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferAuthorizationCreateRequest:
    r"""Defines the request schema for `/transfer/authorization/create`"""
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount of the transfer (decimal string with two digits of precision e.g. \\"10.00\\")."""
    network: TransferNetwork = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network') }})
    r"""The network or rails used for the transfer.

    For transfers submitted as either `ach` or `same-day-ach` the cutoff for same-day is 3:30 PM Eastern Time and the cutoff for next-day transfers is 5:30 PM Eastern Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable.
    """
    type: TransferType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""
    user: TransferAuthorizationUserInRequest = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""The legal name and other information for the account holder."""
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""The Plaid `access_token` for the account that will be debited or credited. Required if not using `payment_profile_token`."""
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id'), 'exclude': lambda f: f is None }})
    r"""The Plaid `account_id` corresponding to the end-user account that will be debited or credited. Required when creating a transfer using an `access_token`."""
    ach_class: Optional[ACHClass] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ach_class'), 'exclude': lambda f: f is None }})
    r"""Specifies the use case of the transfer. Required for transfers on an ACH network.

    `\"ccd\"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    `\"ppd\"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment

    `\"tel\"` - Telephone-Initiated Entry

    `\"web\"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet
    """
    beacon_session_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('beacon_session_id') }})
    r"""The unique identifier returned by Plaid's [beacon](https://plaid.com/docs/transfer/guarantee/#using-a-beacon) when it is run on your webpage."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    credit_funds_source: Optional[TransferCreditFundsSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_funds_source') }})
    r"""Specifies the source of funds for the transfer. Only valid for `credit` transfers, and defaults to `sweep` if not specified. This field is not specified for `debit` transfers.

    `sweep` - Sweep funds from your funding account
    `prefunded_rtp_credits` - Use your prefunded RTP credit balance with Plaid
    `prefunded_ach_credits` - Use your prefunded ACH credit balance with Plaid
    """
    device: Optional[TransferAuthorizationDevice] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('device'), 'exclude': lambda f: f is None }})
    r"""Information about the device being used to initiate the authorization."""
    funding_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('funding_account_id') }})
    r"""The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. Defaults to the account configured during onboarding."""
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('idempotency_key') }})
    r"""A random key provided by the client, per unique authorization, which expires after 48 hours. Maximum of 50 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create an authorization fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single authorization is created.

    This idempotency key expires after 48 hours, after which the same key can be reused. Failure to provide this key may result in duplicate charges.

    Required for guaranteed ACH customers.
    """
    iso_currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code'), 'exclude': lambda f: f is None }})
    r"""The currency of the transfer amount. The default value is \\"USD\\"."""
    origination_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_account_id'), 'exclude': lambda f: f is None }})
    r"""Plaid's unique identifier for the origination account for this authorization. If not specified, the default account will be used.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    originator_client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('originator_client_id') }})
    r"""The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of another client as a third-party sender (TPS)."""
    payment_profile_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_profile_token'), 'exclude': lambda f: f is None }})
    r"""The payment profile token associated with the Payment Profile that will be debited or credited. Required if not using `access_token`."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    test_clock_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test_clock_id') }})
    r"""Plaid’s unique identifier for a test clock. This field may only be used when using `sandbox` environment. If provided, the `authorization` is created at the `virtual_time` on the provided `test_clock`."""
    user_present: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_present') }})
    r"""If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`."""
    with_guarantee: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('with_guarantee') }})
    r"""If set to `false`, Plaid will not offer a `guarantee_decision` for this request (Guarantee customers only)."""
    

