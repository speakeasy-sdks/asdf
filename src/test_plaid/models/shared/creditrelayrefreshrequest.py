"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Final, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreditRelayRefreshRequest:
    r"""CreditRelayRefreshRequest defines the request schema for `/credit/relay/refresh`"""
    relay_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relay_token') }})
    r"""The `relay_token` granting access to the report you would like to refresh."""
    REPORT_TYPE: Final[str] = dataclasses.field(default='asset', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('report_type') }})
    r"""The report type. It can be `asset`. Income report types are not yet supported."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    webhook: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook') }})
    r"""The URL registered to receive webhooks when the report of a relay token has been refreshed."""
    

