"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass
from test_plaid.models import shared
from typing import Callable, Dict, Tuple, Union


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
    client: requests_http.Session
    security: Union[shared.Security1,Callable[[], shared.Security1]] = None
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '2020-09-14_1.421.0'
    sdk_version: str = '0.13.1'
    gen_version: str = '2.253.0'
    user_agent: str = 'speakeasy-sdk/python 0.13.1 2.253.0 2020-09-14_1.421.0 test-plaid'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
