"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TransactionsRecurringGetRequestOptions:
    r"""An optional object to be used with the request. If specified, `options` must not be `null`."""
    include_personal_finance_category: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_personal_finance_category'), 'exclude': lambda f: f is None }})
    r"""Include the [`personal_finance_category`](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-personal-finance-category) object for each transaction stream in the response.

    All implementations are encouraged to set this field to `true` and to use the `personal_finance_category` field instead of `category`. Personal finance categories are the preferred categorization system for transactions, providing higher accuracy and more meaningful categories.

    See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.
    """
    

