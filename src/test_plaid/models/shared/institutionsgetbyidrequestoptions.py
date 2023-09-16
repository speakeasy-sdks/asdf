"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InstitutionsGetByIDRequestOptions:
    r"""Specifies optional parameters for `/institutions/get_by_id`. If provided, must not be `null`."""
    include_auth_metadata: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_auth_metadata'), 'exclude': lambda f: f is None }})
    r"""When `true`, returns metadata related to the Auth product indicating which auth methods are supported."""
    include_optional_metadata: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_optional_metadata'), 'exclude': lambda f: f is None }})
    r"""When `true`, return an institution's logo, brand color, and URL. When available, the bank's logo is returned as a base64 encoded 152x152 PNG, the brand color is in hexadecimal format. The default value is `false`.

    Note that Plaid does not own any of the logos shared by the API and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos.
    """
    include_payment_initiation_metadata: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_payment_initiation_metadata'), 'exclude': lambda f: f is None }})
    r"""When `true`, returns metadata related to the Payment Initiation product indicating which payment configurations are supported."""
    include_status: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_status'), 'exclude': lambda f: f is None }})
    r"""If `true`, the response will include status information about the institution. Default value is `false`."""
    

