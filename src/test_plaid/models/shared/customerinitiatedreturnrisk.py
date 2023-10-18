"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomerInitiatedReturnRisk:
    r"""The object contains a risk score and a risk tier that evaluate the transaction return risk of an unauthorized debit. Common return codes in this category include: \\"R05\\", \\"R07\\", \\"R10\\", \\"R11\\", \\"R29\\". These returns typically have a return time frame of up to 60 calendar days. During this period, the customer of financial institutions can dispute a transaction as unauthorized."""
    risk_tier: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk_tier') }})
    r"""A tier corresponding to the projected likelihood that the transaction, if initiated, will be subject to a return.

    In the `customer_initiated_return_risk` object, there are five risk tiers corresponding to the scores:
      1: Predicted customer-initiated return incidence rate between 0.00% - 0.02%
      2: Predicted customer-initiated return incidence rate between 0.02% - 0.05%
      3: Predicted customer-initiated return incidence rate between 0.05% - 0.1%
      4: Predicted customer-initiated return incidence rate between 0.1% - 0.5%
      5: Predicted customer-initiated return incidence rate greater than 0.5%
    """
    score: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score') }})
    r"""A score from 1-99 that indicates the transaction return risk: a higher risk score suggests a higher return likelihood."""
    

