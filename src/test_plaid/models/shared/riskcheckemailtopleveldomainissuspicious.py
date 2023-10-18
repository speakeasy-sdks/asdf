"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class RiskCheckEmailTopLevelDomainIsSuspicious(str, Enum):
    r"""Indicates whether the email address top level domain, which is the last part of the domain, is fraudulent or risky if known. In most cases, a suspicious top level domain is also associated with a disposable or high-risk domain."""
    YES = 'yes'
    NO = 'no'
    NO_DATA = 'no_data'