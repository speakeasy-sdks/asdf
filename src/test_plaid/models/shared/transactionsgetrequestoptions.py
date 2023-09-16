"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TransactionsGetRequestOptions:
    r"""An optional object to be used with the request. If specified, `options` must not be `null`."""
    account_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_ids'), 'exclude': lambda f: f is None }})
    r"""A list of `account_ids` to retrieve for the Item

    Note: An error will be returned if a provided `account_id` is not associated with the Item.
    """
    count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count'), 'exclude': lambda f: f is None }})
    r"""The number of transactions to fetch."""
    include_logo_and_counterparty_beta: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_logo_and_counterparty_beta'), 'exclude': lambda f: f is None }})
    r"""Include counterparties and extran merchant fields in the transaction. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager."""
    include_original_description: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_original_description'), 'exclude': lambda f: f is None }})
    r"""Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager, or submit a [Support request](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/product-functionality) ."""
    include_personal_finance_category: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_personal_finance_category'), 'exclude': lambda f: f is None }})
    r"""Include the [`personal_finance_category`](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-personal-finance-category) object in the response.

    All implementations are encouraged to set this field to `true` and use the `personal_finance_category` instead of `category`. Personal finance categories are the preferred categorization system for transactions, providing higher accuracy and more meaningful categories.

    See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.
    """
    include_personal_finance_category_beta: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_personal_finance_category_beta'), 'exclude': lambda f: f is None }})
    r"""Please use [`include_personal_finance_category`](https://plaid.com/docs/api/products/transactions/#transactions-get-request-options-include-personal-finance-category) instead.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    offset: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offset'), 'exclude': lambda f: f is None }})
    r"""The number of transactions to skip. The default value is 0."""
    

