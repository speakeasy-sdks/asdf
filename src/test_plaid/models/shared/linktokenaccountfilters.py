"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import creditfilter as shared_creditfilter
from ..shared import depositoryfilter as shared_depositoryfilter
from ..shared import investmentfilter as shared_investmentfilter
from ..shared import loanfilter as shared_loanfilter
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkTokenAccountFilters:
    r"""By default, Link will provide limited account filtering: it will only display Institutions that are compatible with all products supplied in the `products` parameter of `/link/token/create`, and, if `auth` is specified in the `products` array, will also filter out accounts other than `checking` and `savings` accounts on the Account Select pane. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `\\"all\\"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema).

    For institutions using OAuth, the filter will not affect the list of accounts shown by the bank in the OAuth window.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    credit: Optional[shared_creditfilter.CreditFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit'), 'exclude': lambda f: f is None }})
    r"""A filter to apply to `credit`-type accounts"""
    depository: Optional[shared_depositoryfilter.DepositoryFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('depository'), 'exclude': lambda f: f is None }})
    r"""A filter to apply to `depository`-type accounts"""
    investment: Optional[shared_investmentfilter.InvestmentFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('investment'), 'exclude': lambda f: f is None }})
    r"""A filter to apply to `investment`-type accounts (or `brokerage`-type accounts for API versions 2018-05-22 and earlier)."""
    loan: Optional[shared_loanfilter.LoanFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loan'), 'exclude': lambda f: f is None }})
    r"""A filter to apply to `loan`-type accounts"""
    
