"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class PaymentInitiationConsentScope(str, Enum):
    r"""Payment consent scope. Defines possible directions for payments made with the given consent.

    `ME_TO_ME`: Allows moving money between accounts owned by the same user.

    `EXTERNAL`: Allows initiating payments from the user's account to third parties.
    """
    ME_TO_ME = 'ME_TO_ME'
    EXTERNAL = 'EXTERNAL'
