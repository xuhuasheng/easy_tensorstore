"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 15:10:27
LastEditTime : 2024-01-10 11:09:13
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import Optional, Union, Literal
from easy_tensorstore.context_fx import Context, ContextResource
from easy_tensorstore.constant import KVSTORE_DRIVER
from .kvstore import KvStore



class GcsUserProject(ContextResource):
    def __init__(self, 
                 project_id: Optional[str] = None) -> None:
        super().__init__()
        self.project_id  = project_id 

class GcsRequestConcurrency(ContextResource):
    def __init__(self, 
                 limit: Optional[Union[int, Literal["shared"]]] = "shared") -> None:
        super().__init__()
        self.limit = limit

class GcsRequestRetries(ContextResource):
    def __init__(self, 
                 max_retries: Optional[int] = 32,
                 initial_delay: str = "1s",
                 max_delay: str = "32s") -> None:
        super().__init__()
        self.max_retries  = max_retries
        self.initial_delay = initial_delay
        self.max_delay = max_delay


class GcsKvStore(KvStore):
    """https://google.github.io/tensorstore/kvstore/gcs/index.html#gcs-key-value-store-driver
    Args:
        https://google.github.io/tensorstore/kvstore/gcs/index.html#json-kvstore/gcs"""
    def __init__(self, 
                 bucket: str,
                 *,
                 path: Optional[str] = None,
                 context: Optional[Context] = None,
                 gcs_request_concurrency: Optional[GcsRequestConcurrency] = None,
                 gcs_user_project: Optional[GcsUserProject] = None,
                 gcs_request_retries: Optional[GcsRequestRetries] = None) -> None:
        super().__init__(KVSTORE_DRIVER.gcs)
        self.bucket = bucket
        self.path = path
        self.context = context
        self.gcs_request_concurrency = gcs_request_concurrency
        self.gcs_user_project = gcs_user_project
        self.gcs_request_retries = gcs_request_retries

