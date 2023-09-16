"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import itemimportrequestoptions as shared_itemimportrequestoptions
from ..shared import itemimportrequestuserauth as shared_itemimportrequestuserauth
from ..shared import products as shared_products
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ItemImportRequest:
    r"""ItemImportRequest defines the request schema for `/item/import`"""
    products: list[shared_products.Products] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('products') }})
    r"""Array of product strings"""
    user_auth: shared_itemimportrequestuserauth.ItemImportRequestUserAuth = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_auth') }})
    r"""Object of user ID and auth token pair, permitting Plaid to aggregate a user’s accounts"""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    options: Optional[shared_itemimportrequestoptions.ItemImportRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""An optional object to configure `/item/import` request."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

