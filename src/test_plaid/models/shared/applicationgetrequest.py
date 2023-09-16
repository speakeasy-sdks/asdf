"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ApplicationGetRequest:
    r"""ApplicationGetRequest defines the schema for `/application/get`"""
    application_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_id') }})
    r"""This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    
