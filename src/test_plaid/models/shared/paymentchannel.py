"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class PaymentChannel(str, Enum):
    r"""The channel used to make a payment.
    `online:` transactions that took place online.

    `in store:` transactions that were made at a physical location.

    `other:` transactions that relate to banks, e.g. fees or deposits.
    """
    ONLINE = 'online'
    IN_STORE = 'in store'
    OTHER = 'other'