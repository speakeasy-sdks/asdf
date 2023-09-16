"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TransferQuestionnaireCreateRequest:
    r"""Defines the request schema for `/transfer/questionnaire/create`"""
    originator_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('originator_client_id') }})
    r"""Client ID of the end customer."""
    redirect_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirect_uri') }})
    r"""URL the end customer will be redirected to after completing questions in Plaid-hosted onboarding flow."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

