"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .incomeverificationcreaterequestoptions import IncomeVerificationCreateRequestOptions
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IncomeVerificationCreateRequest:
    r"""IncomeVerificationCreateRequest defines the request schema for `/income/verification/create`"""
    webhook: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook') }})
    r"""The URL endpoint to which Plaid should send webhooks related to the progress of the income verification process."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    options: Optional[IncomeVerificationCreateRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""Optional arguments for `/income/verification/create`"""
    precheck_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('precheck_id'), 'exclude': lambda f: f is None }})
    r"""The ID of a precheck created with `/income/verification/precheck`. Will be used to improve conversion of the income verification flow."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

