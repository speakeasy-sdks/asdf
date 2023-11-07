"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .plaiderrortype import PlaidErrorType
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PlaidError:
    r"""We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues. An Item with a non-`null` error object will only be part of an API response when calling `/item/get` to view Item status. Otherwise, error fields will be `null` if no error has occurred; if an error has occurred, an error code will be returned instead."""
    display_message: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_message') }})
    r"""A user-friendly representation of the error code. `null` if the error is not related to user action.

    This may change over time and is not safe for programmatic use.
    """
    error_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_code') }})
    r"""The particular error code. Safe for programmatic use."""
    error_message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_message') }})
    r"""A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use."""
    error_type: PlaidErrorType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_type') }})
    r"""A broad categorization of the error. Safe for programmatic use."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    causes: Optional[List[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('causes'), 'exclude': lambda f: f is None }})
    r"""In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, `causes` will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.

    `causes` will only be provided for the `error_type` `ASSET_REPORT_ERROR`. `causes` will also not be populated inside an error nested within a `warning` object.
    """
    documentation_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documentation_url'), 'exclude': lambda f: f is None }})
    r"""The URL of a Plaid documentation page with more information about the error"""
    request_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id'), 'exclude': lambda f: f is None }})
    r"""A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks."""
    status: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook."""
    suggested_action: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suggested_action') }})
    r"""Suggested steps for resolving the error"""
    

