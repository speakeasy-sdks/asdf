"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import bankinitiatedreturnrisk as shared_bankinitiatedreturnrisk
from ..shared import customerinitiatedreturnrisk as shared_customerinitiatedreturnrisk
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SignalScores:
    r"""Risk scoring details broken down by risk category."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    bank_initiated_return_risk: Optional[shared_bankinitiatedreturnrisk.BankInitiatedReturnRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_initiated_return_risk'), 'exclude': lambda f: f is None }})
    r"""The object contains a risk score and a risk tier that evaluate the transaction return risk because an account is overdrawn or because an ineligible account is used. Common return codes in this category include: \\"R01\\", \\"R02\\", \\"R03\\", \\"R04\\", \\"R06\\", \\"R08\\",  \\"R09\\", \\"R13\\", \\"R16\\", \\"R17\\", \\"R20\\", \\"R23\\". These returns have a turnaround time of 2 banking days."""
    customer_initiated_return_risk: Optional[shared_customerinitiatedreturnrisk.CustomerInitiatedReturnRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_initiated_return_risk'), 'exclude': lambda f: f is None }})
    r"""The object contains a risk score and a risk tier that evaluate the transaction return risk of an unauthorized debit. Common return codes in this category include: \\"R05\\", \\"R07\\", \\"R10\\", \\"R11\\", \\"R29\\". These returns typically have a return time frame of up to 60 calendar days. During this period, the customer of financial institutions can dispute a transaction as unauthorized."""
    
