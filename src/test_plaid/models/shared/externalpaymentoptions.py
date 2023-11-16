"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .paymentinitiationoptionalrestrictionbacs import PaymentInitiationOptionalRestrictionBacs
from .paymentscheme import PaymentScheme
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExternalPaymentOptions:
    r"""Additional payment options"""
    bacs: Optional[PaymentInitiationOptionalRestrictionBacs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bacs') }})
    r"""An optional object used to restrict the accounts used for payments. If provided, the end user will be able to send payments only from the specified bank account."""
    iban: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iban') }})
    r"""The International Bank Account Number (IBAN) for the payer's account. Where possible, the end user will be able to send payments only from the specified bank account if provided."""
    request_refund_details: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_refund_details') }})
    r"""When `true`, Plaid will attempt to request refund details from the payee's financial institution.  Support varies between financial institutions and will not always be available.  If refund details could be retrieved, they will be available in the `/payment_initiation/payment/get` response."""
    scheme: Optional[PaymentScheme] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheme') }})
    r"""Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.

    `LOCAL_DEFAULT`: The default payment scheme for the selected market and currency will be used.

    `LOCAL_INSTANT`: The instant payment scheme for the selected market and currency will be used (if applicable). Fees may be applied by the institution. If the market does not support an Instant Scheme (e.g. Denmark), the default in the region will be used.

    `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.

    `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks.
    """
    

