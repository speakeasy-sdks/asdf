"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .incomeverificationprecheckemployer import IncomeVerificationPrecheckEmployer
from .incomeverificationprecheckmilitaryinfo import IncomeVerificationPrecheckMilitaryInfo
from .incomeverificationprecheckpayrollinstitution import IncomeVerificationPrecheckPayrollInstitution
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditPayrollIncomePrecheckRequest:
    r"""Defines the request schema for `/credit/payroll_income/precheck`."""
    UNSET='__SPEAKEASY_UNSET__'
    access_tokens: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_tokens'), 'exclude': lambda f: f is None }})
    r"""An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note that if the Items specified here are not already initialized with `transactions`, providing them in this field will cause these Items to be initialized with (and billed for) the Transactions product."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    employer: Optional[IncomeVerificationPrecheckEmployer] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employer'), 'exclude': lambda f: f is CreditPayrollIncomePrecheckRequest.UNSET }})
    r"""Information about the end user's employer"""
    payroll_institution: Optional[IncomeVerificationPrecheckPayrollInstitution] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payroll_institution'), 'exclude': lambda f: f is CreditPayrollIncomePrecheckRequest.UNSET }})
    r"""Information about the end user's payroll institution"""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    us_military_info: Optional[IncomeVerificationPrecheckMilitaryInfo] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('us_military_info'), 'exclude': lambda f: f is CreditPayrollIncomePrecheckRequest.UNSET }})
    r"""Data about military info in the income verification precheck."""
    user_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_token'), 'exclude': lambda f: f is None }})
    r"""The user token associated with the User data is being requested for."""
    

