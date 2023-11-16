"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class FDXNotificationPayloadIDType(str, Enum):
    r"""Type of entity causing origination of a notification"""
    ACCOUNT = 'ACCOUNT'
    CUSTOMER = 'CUSTOMER'
    PARTY = 'PARTY'
    MAINTENANCE = 'MAINTENANCE'
    CONSENT = 'CONSENT'
