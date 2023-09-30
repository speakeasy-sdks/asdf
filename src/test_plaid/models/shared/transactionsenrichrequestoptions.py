"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TransactionsEnrichRequestOptions:
    r"""An optional object to be used with the request."""
    include_legacy_category: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_legacy_category'), 'exclude': lambda f: f is None }})
    r"""Include `legacy_category` and `legacy_category_id` in the response (in addition to the default `personal_finance_category`).

    Categories are based on Plaid's legacy taxonomy. For a full list of legacy categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).
    """
    

