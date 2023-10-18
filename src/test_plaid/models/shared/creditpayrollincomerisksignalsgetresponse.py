"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import payrollrisksignalsitem as shared_payrollrisksignalsitem
from ..shared import plaiderror as shared_plaiderror
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditPayrollIncomeRiskSignalsGetResponse:
    r"""CreditPayrollIncomeRiskSignalsGetRequest defines the response schema for `/credit/payroll_income/risk_signals/get`"""
    items: List[shared_payrollrisksignalsitem.PayrollRiskSignalsItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    r"""Array of payroll items."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    error: Optional[shared_plaiderror.PlaidError] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    r"""We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues. An Item with a non-`null` error object will only be part of an API response when calling `/item/get` to view Item status. Otherwise, error fields will be `null` if no error has occurred; if an error has occurred, an error code will be returned instead."""
    

