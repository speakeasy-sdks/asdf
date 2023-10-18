"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import incomeverificationprecheckconfidence as shared_incomeverificationprecheckconfidence
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditPayrollIncomePrecheckResponse:
    r"""Defines the response schema for `/credit/payroll_income/precheck`."""
    confidence: shared_incomeverificationprecheckconfidence.IncomeVerificationPrecheckConfidence = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confidence') }})
    r"""The confidence that Plaid can support the user in the digital income verification flow instead of requiring a manual paystub upload. One of the following:

    `\"HIGH\"`: It is very likely that this user can use the digital income verification flow.

    \"`LOW`\": It is unlikely that this user can use the digital income verification flow.

    `\"UNKNOWN\"`: It was not possible to determine if the user is supportable with the information passed.
    """
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

