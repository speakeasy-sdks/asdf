"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass
from typing import Dict, Tuple
from .utils.retries import RetryConfig
from .utils import utils


SERVERS = [
    'https://production.plaid.com',
    # Production
    'https://development.plaid.com',
    # Development
    'https://sandbox.plaid.com',
    # Sandbox
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    security_client: requests.Session
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '2020-09-14_1.421.0'
    sdk_version: str = '0.8.0'
    gen_version: str = '2.181.1'
    user_agent: str = 'speakeasy-sdk/python 0.8.0 2.181.1 2020-09-14_1.421.0 test-plaid'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
