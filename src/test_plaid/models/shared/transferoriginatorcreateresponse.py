"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferOriginatorCreateResponse:
    r"""Defines the response schema for `/transfer/originator/create`"""
    company_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_name') }})
    r"""The company name of the end customer."""
    originator_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('originator_client_id') }})
    r"""Client ID of the originator. This identifier will be used when creating transfers and should be stored associated with end user information."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
