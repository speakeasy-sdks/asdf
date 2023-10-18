"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import paystubpayfrequency as shared_paystubpayfrequency
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaystubDetails:
    r"""An object representing details that can be found on the paystub.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    pay_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat }})
    r"""Pay date on the paystub in the 'YYYY-MM-DD' format."""
    pay_frequency: Optional[shared_paystubpayfrequency.PaystubPayFrequency] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_frequency') }})
    r"""The frequency at which the employee is paid. Possible values: `MONTHLY`, `BI-WEEKLY`, `WEEKLY`, `SEMI-MONTHLY`."""
    pay_period_end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_period_end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat }})
    r"""Ending date of the pay period on the paystub in the 'YYYY-MM-DD' format."""
    pay_period_start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_period_start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat }})
    r"""Beginning date of the pay period on the paystub in the 'YYYY-MM-DD' format."""
    paystub_provider: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paystub_provider') }})
    r"""The name of the payroll provider that generated the paystub, e.g. ADP"""
    
