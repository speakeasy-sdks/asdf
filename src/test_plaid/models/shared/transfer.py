"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .achclass import ACHClass
from .transferauthorizationguaranteedecision import TransferAuthorizationGuaranteeDecision
from .transferauthorizationguaranteedecisionrationale import TransferAuthorizationGuaranteeDecisionRationale
from .transfercreditfundssource import TransferCreditFundsSource
from .transferexpectedsweepsettlementscheduleitem import TransferExpectedSweepSettlementScheduleItem
from .transferfailure import TransferFailure
from .transfernetwork import TransferNetwork
from .transferrefund import TransferRefund
from .transferstatus import TransferStatus
from .transfersweepstatus import TransferSweepStatus
from .transfertype import TransferType
from .transferuserinresponse import TransferUserInResponse
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Transfer:
    r"""Represents a transfer within the Transfers API."""
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount of the transfer (decimal string with two digits of precision e.g. \\"10.00\\")."""
    authorization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization_id') }})
    r"""Plaid’s unique identifier for a transfer authorization."""
    cancellable: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancellable') }})
    r"""When `true`, you can still cancel this transfer."""
    created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`"""
    credit_funds_source: Optional[TransferCreditFundsSource] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_funds_source') }})
    r"""Specifies the source of funds for the transfer. Only valid for `credit` transfers, and defaults to `sweep` if not specified. This field is not specified for `debit` transfers.

    `sweep` - Sweep funds from your funding account
    `prefunded_rtp_credits` - Use your prefunded RTP credit balance with Plaid
    `prefunded_ach_credits` - Use your prefunded ACH credit balance with Plaid
    """
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""The description of the transfer."""
    expected_settlement_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expected_settlement_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The expected date when the full amount of the transfer settles at the consumers’ account, if the transfer is credit; or at the customer's business checking account, if the transfer is debit. Only set for ACH transfers and is null for non-ACH transfers. Only set for ACH transfers. This will be of the form YYYY-MM-DD."""
    failure_reason: Optional[TransferFailure] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failure_reason') }})
    r"""The failure reason if the event type for a transfer is `\\"failed\\"` or `\\"returned\\"`. Null value otherwise."""
    funding_account_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('funding_account_id') }})
    r"""The id of the associated funding account, available in the Plaid Dashboard. If present, this indicates which of your business checking accounts will be credited or debited."""
    guarantee_decision: Optional[TransferAuthorizationGuaranteeDecision] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('guarantee_decision') }})
    r"""Indicates whether the transfer is guaranteed by Plaid (Guarantee customers only). This field will contain either `GUARANTEED` or `NOT_GUARANTEED` indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the `guarantee_decision_rationale` field. Refer to the `code` field in `guarantee_decision_rationale` for details."""
    guarantee_decision_rationale: Optional[TransferAuthorizationGuaranteeDecisionRationale] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('guarantee_decision_rationale') }})
    r"""The rationale for Plaid's decision to not guarantee a transfer. Will be `null` unless `guarantee_decision` is `NOT_GUARANTEED`."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Plaid’s unique identifier for a transfer."""
    iso_currency_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The currency of the transfer amount, e.g. \\"USD\\" """
    metadata: Optional[Dict[str, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    The JSON values must be Strings (no nested JSON objects allowed)
    Only ASCII characters may be used
    Maximum of 50 key/value pairs
    Maximum key length of 40 characters
    Maximum value length of 500 characters
    """
    network: TransferNetwork = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network') }})
    r"""The network or rails used for the transfer.

    For transfers submitted as either `ach` or `same-day-ach` the cutoff for same-day is 3:30 PM Eastern Time and the cutoff for next-day transfers is 5:30 PM Eastern Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable.
    """
    origination_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_account_id') }})
    r"""Plaid’s unique identifier for the origination account that was used for this transfer.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    originator_client_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('originator_client_id') }})
    r"""The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS)."""
    recurring_transfer_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recurring_transfer_id') }})
    r"""The id of the recurring transfer if this transfer belongs to a recurring transfer."""
    refunds: List[TransferRefund] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refunds') }})
    r"""A list of refunds associated with this transfer."""
    standard_return_window: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('standard_return_window'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date 3 business days from settlement date indicating the following ACH returns can no longer happen: R01, R02, R03, R29. This will be of the form YYYY-MM-DD."""
    status: TransferStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the transfer.

    `pending`: A new transfer was created; it is in the pending state.
    `posted`: The transfer has been successfully submitted to the payment network.
    `settled`: Credits are available to be withdrawn or debits have been deducted from the Plaid linked account.
    `cancelled`: The transfer was cancelled by the client.
    `failed`: The transfer failed, no funds were moved.
    `returned`: A posted transfer was returned.
    """
    type: TransferType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""
    unauthorized_return_window: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unauthorized_return_window'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date 61 business days from settlement date indicating the following ACH returns can no longer happen: R05, R07, R10, R11, R51, R33, R37, R38, R51, R52, R53. This will be of the form YYYY-MM-DD."""
    user: TransferUserInResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""The legal name and other information for the account holder."""
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id'), 'exclude': lambda f: f is None }})
    r"""The Plaid `account_id` corresponding to the end-user account that will be debited or credited."""
    ach_class: Optional[ACHClass] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ach_class'), 'exclude': lambda f: f is None }})
    r"""Specifies the use case of the transfer. Required for transfers on an ACH network.

    `\"ccd\"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    `\"ppd\"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment

    `\"tel\"` - Telephone-Initiated Entry

    `\"web\"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    expected_sweep_settlement_schedule: Optional[List[TransferExpectedSweepSettlementScheduleItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expected_sweep_settlement_schedule'), 'exclude': lambda f: f is None }})
    r"""The expected sweep settlement schedule of this transfer, assuming this transfer is not `returned`. Only applies to ACH debit transfers."""
    sweep_status: Optional[TransferSweepStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sweep_status') }})
    r"""The status of the sweep for the transfer.

    `unswept`: The transfer hasn't been swept yet.
    `swept`: The transfer was swept to the sweep account.
    `swept_settled`: Credits are available to be withdrawn or debits have been deducted from the customer’s business checking account.
    `return_swept`: The transfer was returned, funds were pulled back or pushed back to the sweep account.
    `null`: The transfer will never be swept (e.g. if the transfer is cancelled or returned before being swept)
    """
    

