"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .walletpaymentscheme import WalletPaymentScheme
from .wallettransactionamount import WalletTransactionAmount
from .wallettransactioncounterparty import WalletTransactionCounterparty
from .wallettransactionfailurereason import WalletTransactionFailureReason
from .wallettransactionstatus import WalletTransactionStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from test_plaid import utils
from typing import Any, Dict, Optional

class WalletTransactionGetResponseType(str, Enum):
    r"""The type of the transaction. The supported transaction types that are returned are:
    `BANK_TRANSFER:` a transaction which credits an e-wallet through an external bank transfer.

    `PAYOUT:` a transaction which debits an e-wallet by disbursing funds to a counterparty.

    `PIS_PAY_IN:` a payment which credits an e-wallet through Plaid's Payment Initiation Services (PIS) APIs. For more information see the [Payment Initiation endpoints](https://plaid.com/docs/api/products/payment-initiation/).

    `REFUND:` a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid's [PIS APIs](https://plaid.com/docs/api/products/payment-initiation/).

    `FUNDS_SWEEP`: an automated transaction which debits funds from an e-wallet to a designated client-owned account.
    """
    BANK_TRANSFER = 'BANK_TRANSFER'
    PAYOUT = 'PAYOUT'
    PIS_PAY_IN = 'PIS_PAY_IN'
    REFUND = 'REFUND'
    FUNDS_SWEEP = 'FUNDS_SWEEP'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletTransactionGetResponse:
    r"""The transaction details"""
    amount: WalletTransactionAmount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount and currency of a transaction"""
    counterparty: WalletTransactionCounterparty = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('counterparty') }})
    r"""An object representing the e-wallet transaction's counterparty"""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Timestamp when the transaction was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    last_status_update: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_status_update'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time of the last time the `status` was updated, in IS0 8601 format"""
    reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference') }})
    r"""A reference for the transaction"""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    status: WalletTransactionStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the transaction.

    `AUTHORISING`: The transaction is being processed for validation and compliance.

    `INITIATED`: The transaction has been initiated and is currently being processed.

    `EXECUTED`: The transaction has been successfully executed and is considered complete. This is only applicable for debit transactions.

    `SETTLED`: The transaction has settled and funds are available for use. This is only applicable for credit transactions. A transaction will typically settle within seconds to several days, depending on which payment rail is used.

    `FAILED`: The transaction failed to process successfully. This is a terminal status.

    `BLOCKED`: The transaction has been blocked for violating compliance rules. This is a terminal status.
    """
    transaction_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_id') }})
    r"""A unique ID identifying the transaction"""
    type: WalletTransactionGetResponseType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of the transaction. The supported transaction types that are returned are:
    `BANK_TRANSFER:` a transaction which credits an e-wallet through an external bank transfer.

    `PAYOUT:` a transaction which debits an e-wallet by disbursing funds to a counterparty.

    `PIS_PAY_IN:` a payment which credits an e-wallet through Plaid's Payment Initiation Services (PIS) APIs. For more information see the [Payment Initiation endpoints](https://plaid.com/docs/api/products/payment-initiation/).

    `REFUND:` a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid's [PIS APIs](https://plaid.com/docs/api/products/payment-initiation/).

    `FUNDS_SWEEP`: an automated transaction which debits funds from an e-wallet to a designated client-owned account.
    """
    wallet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallet_id') }})
    r"""The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    failure_reason: Optional[WalletTransactionFailureReason] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failure_reason') }})
    r"""The error code of a failed transaction. Error codes include:
    `EXTERNAL_SYSTEM`: The transaction was declined by an external system.
    `EXPIRED`: The transaction request has expired.
    `CANCELLED`: The transaction request was rescinded.
    `INVALID`: The transaction did not meet certain criteria, such as an inactive account or no valid counterparty, etc.
    `UNKNOWN`: The transaction was unsuccessful, but the exact cause is unknown.
    """
    payment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_id') }})
    r"""The payment id that this transaction is associated with, if any. This is present only for transaction types `PIS_PAY_IN` and `REFUND`."""
    scheme: Optional[WalletPaymentScheme] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheme') }})
    r"""The payment scheme used to execute this transaction. This is present only for transaction types `PAYOUT` and `REFUND`.

    `FASTER_PAYMENTS`: The standard payment scheme within the UK.

    `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.

    `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment to a beneficiary within the SEPA area.
    """
    

