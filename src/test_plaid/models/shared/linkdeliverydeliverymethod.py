"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class LinkDeliveryDeliveryMethod(str, Enum):
    r"""The delivery method to be used to deliver the Hosted Link session URL.

    `SMS`: The URL will be delivered through SMS

    `EMAIL`: The URL will be delivered through email
    """
    SMS = 'SMS'
    EMAIL = 'EMAIL'