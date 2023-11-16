"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .transactionsrecurringgetrequestoptions import TransactionsRecurringGetRequestOptions
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProcessorTransactionsRecurringGetRequest:
    r"""ProcessorTransactionsRecurringGetRequest defines the request schema for `/processor/transactions/recurring/get`"""
    account_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_ids') }})
    r"""A list of `account_ids` to retrieve for the Item

    Note: An error will be returned if a provided `account_id` is not associated with the Item.
    """
    processor_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processor_token') }})
    r"""The processor token obtained from the Plaid integration partner. Processor tokens are in the format: `processor-<environment>-<identifier>`"""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    options: Optional[TransactionsRecurringGetRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""An optional object to be used with the request. If specified, `options` must not be `null`."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

