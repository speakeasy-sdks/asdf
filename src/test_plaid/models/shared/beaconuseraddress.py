"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BeaconUserAddress:
    r"""Even if an address has been collected, some fields may be null depending on the region's addressing system. For example:


    Addresses from the United Kingdom will not include a region


    Addresses from Hong Kong will not include a postal code
    """
    city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    r"""City from the end user's address"""
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form."""
    postal_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code') }})
    r"""The postal code for the associated address. Between 2 and 10 alphanumeric characters. For US-based addresses this must be 5 numeric digits."""
    region: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""An ISO 3166-2 subdivision code. Related terms would be \\"state\\", \\"province\\", \\"prefecture\\", \\"zone\\", \\"subdivision\\", etc."""
    street: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street') }})
    r"""The primary street portion of an address. If the user has submitted their address, this field will always be filled."""
    street2: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street2') }})
    r"""Extra street information, like an apartment or suite number."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
