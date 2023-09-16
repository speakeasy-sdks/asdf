"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class FDXNotificationSeverity(str, Enum):
    r"""Severity level of notification"""
    EMERGENCY = 'EMERGENCY'
    ALERT = 'ALERT'
    WARNING = 'WARNING'
    NOTICE = 'NOTICE'
    INFO = 'INFO'