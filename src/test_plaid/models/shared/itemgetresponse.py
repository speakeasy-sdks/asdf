"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .item import Item
from .itemstatusnullable import ItemStatusNullable
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ItemGetResponse:
    r"""ItemGetResponse defines the response schema for `/item/get` and `/item/webhook/update`"""
    item: Item = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item') }})
    r"""Metadata about the Item."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    status: Optional[ItemStatusNullable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Information about the last successful and failed transactions update for the Item."""
    

