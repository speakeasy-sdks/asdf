"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkOAuthCorrelationIDExchangeResponse:
    r"""LinkOAuthCorrelationIdExchangeResponse defines the response schema for `/link/oauth/correlation_id/exchange`"""
    link_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_token') }})
    r"""The `link_token` associated to the given `link_correlation_id`, which can be used to re-initialize Link."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

