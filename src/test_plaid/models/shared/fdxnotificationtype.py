"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class FDXNotificationType(str, Enum):
    r"""Type of Notification"""
    CONSENT_REVOKED = 'CONSENT_REVOKED'
    CONSENT_UPDATED = 'CONSENT_UPDATED'
    CUSTOM = 'CUSTOM'
    SERVICE = 'SERVICE'
    BALANCE = 'BALANCE'
    PLANNED_OUTAGE = 'PLANNED_OUTAGE'
