"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .paymentamount import PaymentAmount
from .paymentconsentperiodicalignment import PaymentConsentPeriodicAlignment
from .paymentconsentperiodicinterval import PaymentConsentPeriodicInterval
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentConsentPeriodicAmount:
    r"""Defines consent payments limitations per period."""
    alignment: PaymentConsentPeriodicAlignment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alignment') }})
    r"""Where the payment consent period should start.

    `CALENDAR`: line up with a calendar.

    `CONSENT`: on the date of consent creation.
    """
    amount: PaymentAmount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""Maximum cumulative amount for all payments in the specified interval."""
    interval: PaymentConsentPeriodicInterval = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval') }})
    r"""Payment consent periodic interval."""
    

