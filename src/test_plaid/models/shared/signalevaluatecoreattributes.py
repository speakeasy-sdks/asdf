"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SignalEvaluateCoreAttributes:
    r"""The core attributes object contains additional data that can be used to assess the ACH return risk. Examples of data include:

    `days_since_first_plaid_connection`: The number of days since the first time the Item was connected to an application via Plaid
    `plaid_connections_count_7d`: The number of times the Item has been connected to applications via Plaid over the past 7 days
    `plaid_connections_count_30d`: The number of times the Item has been connected to applications via Plaid over the past 30 days
    `total_plaid_connections_count`: The number of times the Item has been connected to applications via Plaid
    `is_savings_or_money_market_account`: Indicates whether the ACH transaction funding account is a savings/money market account

    For the full list and detailed documentation of core attributes available, or to request that core attributes not be returned, contact Sales or your Plaid account manager
    """
    UNSET='__SPEAKEASY_UNSET__'
    address_change_count_28d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_change_count_28d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of times the account's addresses on file have changed over the past 28 days"""
    address_change_count_90d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_change_count_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of times the account's addresses on file have changed over the past 90 days"""
    available_balance: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('available_balance'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""Available balance, as of the `balance_last_updated` time. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account."""
    balance_last_updated: Optional[datetime] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance_last_updated'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the balance for the given account has been updated."""
    credit_transactions_count_10d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_transactions_count_10d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total number of credit (inflow) transactions over the past 10 days from the account that will be debited"""
    credit_transactions_count_30d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_transactions_count_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total number of credit (inflow) transactions over the past 30 days from the account that will be debited"""
    credit_transactions_count_60d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_transactions_count_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total number of credit (inflow) transactions over the past 60 days from the account that will be debited"""
    credit_transactions_count_90d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_transactions_count_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total number of credit (inflow) transactions over the past 90 days from the account that will be debited"""
    current_balance: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_balance'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""Current balance, as of the `balance_last_updated` time. The current balance is the total amount of funds in the account."""
    days_since_first_plaid_connection: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_since_first_plaid_connection'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of days since the first time the Item was connected to an application via Plaid"""
    days_with_negative_balance_count_90d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_with_negative_balance_count_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of days within the past 90 days when the account that will be debited had a negative end-of-day available balance"""
    debit_transactions_count_10d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('debit_transactions_count_10d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total number of debit (outflow) transactions over the past 10 days from the account that will be debited"""
    debit_transactions_count_30d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('debit_transactions_count_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total number of debit (outflow) transactions over the past 30 days from the account that will be debited"""
    debit_transactions_count_60d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('debit_transactions_count_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total number of debit (outflow) transactions over the past 60 days from the account that will be debited"""
    debit_transactions_count_90d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('debit_transactions_count_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total number of debit (outflow) transactions over the past 90 days from the account that will be debited"""
    email_change_count_28d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_change_count_28d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of times the account's email addresses on file have changed over the past 28 days"""
    email_change_count_90d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_change_count_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of times the account's email addresses on file have changed over the past 90 days"""
    failed_plaid_non_oauth_authentication_attempts_count_30d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_plaid_non_oauth_authentication_attempts_count_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days"""
    failed_plaid_non_oauth_authentication_attempts_count_3d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_plaid_non_oauth_authentication_attempts_count_3d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days"""
    failed_plaid_non_oauth_authentication_attempts_count_7d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_plaid_non_oauth_authentication_attempts_count_7d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days"""
    is_savings_or_money_market_account: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_savings_or_money_market_account'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""Indicates if the ACH transaction funding account is a savings/money market account"""
    nsf_overdraft_transactions_count_30d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nsf_overdraft_transactions_count_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 30 days from the account that will be debited."""
    nsf_overdraft_transactions_count_60d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nsf_overdraft_transactions_count_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 60 days from the account that will be debited."""
    nsf_overdraft_transactions_count_7d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nsf_overdraft_transactions_count_7d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 7 days from the account that will be debited."""
    nsf_overdraft_transactions_count_90d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nsf_overdraft_transactions_count_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 90 days from the account that will be debited."""
    p10_eod_balance_30d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p10_eod_balance_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 10th percentile of the end-of-day available balance over the past 30 days of the account that will be debited"""
    p10_eod_balance_31d_to_60d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p10_eod_balance_31d_to_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 10th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited"""
    p10_eod_balance_60d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p10_eod_balance_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 10th percentile of the end-of-day available balance over the past 60 days of the account that will be debited"""
    p10_eod_balance_61d_to_90d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p10_eod_balance_61d_to_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 10th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited"""
    p10_eod_balance_90d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p10_eod_balance_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 10th percentile of the end-of-day available balance over the past 90 days of the account that will be debited"""
    p50_credit_transactions_amount_28d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p50_credit_transactions_amount_28d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 50th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited"""
    p50_debit_transactions_amount_28d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p50_debit_transactions_amount_28d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 50th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited"""
    p50_eod_balance_30d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p50_eod_balance_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 50th percentile of the end-of-day available balance over the past 30 days of the account that will be debited"""
    p50_eod_balance_31d_to_60d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p50_eod_balance_31d_to_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 50th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited"""
    p50_eod_balance_60d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p50_eod_balance_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 50th percentile of the end-of-day available balance over the past 60 days of the account that will be debited"""
    p50_eod_balance_61d_to_90d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p50_eod_balance_61d_to_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 50th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited"""
    p50_eod_balance_90d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p50_eod_balance_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 50th percentile of the end-of-day available balance over the past 90 days of the account that will be debited"""
    p90_eod_balance_30d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p90_eod_balance_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 90th percentile of the end-of-day available balance over the past 30 days of the account that will be debited"""
    p90_eod_balance_31d_to_60d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p90_eod_balance_31d_to_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 90th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited"""
    p90_eod_balance_60d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p90_eod_balance_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 90th percentile of the end-of-day available balance over the past 60 days of the account that will be debited"""
    p90_eod_balance_61d_to_90d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p90_eod_balance_61d_to_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 90th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited"""
    p90_eod_balance_90d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p90_eod_balance_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 90th percentile of the end-of-day available balance over the past 90 days of the account that will be debited"""
    p95_credit_transactions_amount_28d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p95_credit_transactions_amount_28d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 95th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited"""
    p95_debit_transactions_amount_28d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('p95_debit_transactions_amount_28d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The 95th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited"""
    phone_change_count_28d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_change_count_28d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of times the account's phone numbers on file have changed over the past 28 days"""
    phone_change_count_90d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_change_count_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of times the account's phone numbers on file have changed over the past 90 days"""
    plaid_connections_count_30d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plaid_connections_count_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of times the Item has been connected to applications via Plaid over the past 30 days"""
    plaid_connections_count_7d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plaid_connections_count_7d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of times the Item has been connected to applications via Plaid over the past 7 days"""
    plaid_non_oauth_authentication_attempts_count_30d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plaid_non_oauth_authentication_attempts_count_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days"""
    plaid_non_oauth_authentication_attempts_count_3d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plaid_non_oauth_authentication_attempts_count_3d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days"""
    plaid_non_oauth_authentication_attempts_count_7d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plaid_non_oauth_authentication_attempts_count_7d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days"""
    total_credit_transactions_amount_10d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_credit_transactions_amount_10d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total credit (inflow) transaction amount over the past 10 days from the account that will be debited"""
    total_credit_transactions_amount_30d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_credit_transactions_amount_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total credit (inflow) transaction amount over the past 30 days from the account that will be debited"""
    total_credit_transactions_amount_60d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_credit_transactions_amount_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total credit (inflow) transaction amount over the past 60 days from the account that will be debited"""
    total_credit_transactions_amount_90d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_credit_transactions_amount_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total credit (inflow) transaction amount over the past 90 days from the account that will be debited"""
    total_debit_transactions_amount_10d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_debit_transactions_amount_10d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total debit (outflow) transaction amount over the past 10 days from the account that will be debited"""
    total_debit_transactions_amount_30d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_debit_transactions_amount_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total debit (outflow) transaction amount over the past 30 days from the account that will be debited"""
    total_debit_transactions_amount_60d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_debit_transactions_amount_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total debit (outflow) transaction amount over the past 60 days from the account that will be debited"""
    total_debit_transactions_amount_90d: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_debit_transactions_amount_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total debit (outflow) transaction amount over the past 90 days from the account that will be debited"""
    total_plaid_connections_count: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_plaid_connections_count'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""The total number of times the Item has been connected to applications via Plaid"""
    transactions_last_updated: Optional[datetime] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions_last_updated'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the transactions for the given account have been updated."""
    unauthorized_transactions_count_30d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unauthorized_transactions_count_30d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 30 days from the account that will be debited."""
    unauthorized_transactions_count_60d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unauthorized_transactions_count_60d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 60 days from the account that will be debited."""
    unauthorized_transactions_count_7d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unauthorized_transactions_count_7d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 7 days from the account that will be debited."""
    unauthorized_transactions_count_90d: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unauthorized_transactions_count_90d'), 'exclude': lambda f: f is SignalEvaluateCoreAttributes.UNSET }})
    r"""We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 90 days from the account that will be debited."""
    

