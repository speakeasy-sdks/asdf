"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .plaiderror import PlaidError
from .products import Products
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from test_plaid import utils
from typing import Any, Dict, List, Optional

class UpdateType(str, Enum):
    r"""Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some forms of two-factor authentication.

    `background` - Item can be updated in the background

    `user_present_required` - Item requires user interaction to be updated
    """
    BACKGROUND = 'background'
    USER_PRESENT_REQUIRED = 'user_present_required'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Item:
    r"""Metadata about the Item."""
    UNSET='__SPEAKEASY_UNSET__'
    available_products: List[Products] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('available_products') }})
    r"""A list of products available for the Item that have not yet been accessed. The contents of this array will be mutually exclusive with `billed_products`."""
    billed_products: List[Products] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billed_products') }})
    r"""A list of products that have been billed for the Item. The contents of this array will be mutually exclusive with `available_products`. Note - `billed_products` is populated in all environments but only requests in Production are billed. Also note that products that are billed on a pay-per-call basis rather than a pay-per-Item basis, such as `balance`, will not appear here."""
    consent_expiration_time: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consent_expiration_time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The RFC 3339 timestamp after which the consent provided by the end user will expire. Upon consent expiration, the item will enter the `ITEM_LOGIN_REQUIRED` error state. To circumvent the `ITEM_LOGIN_REQUIRED` error and maintain continuous consent, the end user can reauthenticate via Link’s update mode in advance of the consent expiration time.

    Note - This is only relevant for certain OAuth-based institutions. For all other institutions, this field will be null.
    """
    error: Optional[PlaidError] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    r"""We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues. An Item with a non-`null` error object will only be part of an API response when calling `/item/get` to view Item status. Otherwise, error fields will be `null` if no error has occurred; if an error has occurred, an error code will be returned instead."""
    item_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item_id') }})
    r"""The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive."""
    update_type: UpdateType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('update_type') }})
    r"""Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some forms of two-factor authentication.

    `background` - Item can be updated in the background

    `user_present_required` - Item requires user interaction to be updated
    """
    webhook: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook') }})
    r"""The URL registered to receive webhooks for the Item."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    consented_products: Optional[List[Products]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consented_products'), 'exclude': lambda f: f is None }})
    r"""A list of products that have gone through consent collection for the Item. Only present for those enabled in the [Data Transparency](https://plaid.com/docs/link/data-transparency-messaging-migration-guide) beta. If you are not enrolled in Data Transparency, this field is not used."""
    institution_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_id'), 'exclude': lambda f: f is Item.UNSET }})
    r"""The Plaid Institution ID associated with the Item. Field is `null` for Items created via Same Day Micro-deposits."""
    products: Optional[List[Products]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('products'), 'exclude': lambda f: f is None }})
    r"""A list of initialized products for the Item. In almost all cases, this will be the same as the `billed_products` field. For some products, it is possible for the product to be initialized on an Item but not yet billed (e.g. Assets, before `/asset_report/create` has been called), in which case the product may appear in `products` but not in `billed_products`."""
    

