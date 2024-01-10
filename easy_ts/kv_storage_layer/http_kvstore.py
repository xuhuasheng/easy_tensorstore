"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 15:26:49
LastEditTime : 2024-01-10 11:07:42
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from typing import List, Literal, Optional, Union

from easy_ts.constant import KVSTORE_DRIVER
from easy_ts.context_fx import ContextResource

from .kvstore import KvStore


class HttpRequestConcurrency(ContextResource):
    def __init__(self, 
                 limit: Optional[Union[int, Literal["shared"]]] = "shared") -> None:
        super().__init__()
        self.limit = limit

class HttpRequestRetries(ContextResource):
    def __init__(self, 
                 max_retries: Optional[int] = 32,
                 initial_delay: str = "1s",
                 max_delay: str = "32s") -> None:
        super().__init__()
        self.max_retries  = max_retries
        self.initial_delay = initial_delay
        self.max_delay = max_delay


class HttpKvStore(KvStore):
    def __init__(self, 
                 base_url: str,
                 *,
                 path: Optional[str] = None,
                 headers: Optional[List[List]] = None,
                 http_request_concurrency : Optional[HttpRequestConcurrency] = None,
                 http_request_retries: Optional[HttpRequestRetries] = None,
                 ) -> None:
        super().__init__(KVSTORE_DRIVER.http)
        self.base_url = base_url
        self.path = path
        self.headers = headers
        self.http_request_concurrency = http_request_concurrency
        self.http_request_retries = http_request_retries