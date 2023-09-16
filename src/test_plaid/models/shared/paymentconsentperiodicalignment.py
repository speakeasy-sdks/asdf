"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class PaymentConsentPeriodicAlignment(str, Enum):
    r"""Where the payment consent period should start.

    `CALENDAR`: line up with a calendar.

    `CONSENT`: on the date of consent creation.
    """
    CALENDAR = 'CALENDAR'
    CONSENT = 'CONSENT'
