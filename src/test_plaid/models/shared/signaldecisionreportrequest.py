"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .signaldecisionoutcome import SignalDecisionOutcome
from .signalpaymentmethod import SignalPaymentMethod
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SignalDecisionReportRequest:
    r"""SignalDecisionReportRequest defines the request schema for `/signal/decision/report`"""
    UNSET='__SPEAKEASY_UNSET__'
    client_transaction_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_transaction_id') }})
    r"""Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`"""
    initiated: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initiated') }})
    r"""`true` if the ACH transaction was initiated, `false` otherwise.

    This field must be returned as a boolean. If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.
    """
    amount_instantly_available: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_instantly_available'), 'exclude': lambda f: f is SignalDecisionReportRequest.UNSET }})
    r"""The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05)."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    days_funds_on_hold: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_funds_on_hold'), 'exclude': lambda f: f is SignalDecisionReportRequest.UNSET }})
    r"""The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.

    For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization.
    """
    decision_outcome: Optional[SignalDecisionOutcome] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('decision_outcome'), 'exclude': lambda f: f is SignalDecisionReportRequest.UNSET }})
    r"""The payment decision from the risk assessment.

    `APPROVE`: approve the transaction without requiring further actions from your customers. For example, use this field if you are placing a standard hold for all the approved transactions before making funds available to your customers. You should also use this field if you decide to accelerate the fund availability for your customers.

    `REVIEW`: the transaction requires manual review

    `REJECT`: reject the transaction

    `TAKE_OTHER_RISK_MEASURES`: for example, placing a longer hold on funds than those approved transactions or introducing customer frictions such as step-up verification/authentication

    `NOT_EVALUATED`: if only logging the Signal results without using them

    Possible values:  `APPROVE`, `REVIEW`, `REJECT`, `TAKE_OTHER_RISK_MEASURES`, `NOT_EVALUATED`
    """
    payment_method: Optional[SignalPaymentMethod] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_method'), 'exclude': lambda f: f is SignalDecisionReportRequest.UNSET }})
    r"""The payment method to complete the transaction after the risk assessment. It may be different from the default payment method.

    `SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day

    `NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors

    `STANDARD_ACH`: standard ACH by NACHA

    `REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow

    `DEBIT_CARD`: if the default payment is over debit card networks

    `MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods

    Possible values: `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`
    """
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

