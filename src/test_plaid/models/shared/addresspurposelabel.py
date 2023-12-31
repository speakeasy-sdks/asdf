"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class AddressPurposeLabel(str, Enum):
    r"""Field describing whether the associated address is being used for commercial or residential purposes.

    Note: This value will be `no_data` when Plaid does not have sufficient data to determine the address's use.
    """
    RESIDENTIAL = 'residential'
    COMMERCIAL = 'commercial'
    NO_DATA = 'no_data'
