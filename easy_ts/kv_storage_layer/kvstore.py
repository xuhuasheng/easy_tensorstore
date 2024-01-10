"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 17:07:32
LastEditTime : 2024-01-10 11:07:06
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

"""Most TensorStore drivers access the underlying storage for array data 
through a key-value store layer that supports a variety of underlying 
storage systems, such as the local filesystem and cloud storage systems, 
through different drivers."""


from typing import Optional, TypeVar

from easy_ts.constant import KVSTORE_DRIVER
from easy_ts.context_fx import Context
from easy_ts.json_base import JsonBase


class KvStore(JsonBase):
    """Key-value store specification.
    This describes the common properties supported by all key-value stores. 
    Refer to the driver documentation for the supported driver identifiers 
    and driver-specific properties.
    https://google.github.io/tensorstore/kvstore/index.html#json-KvStore"""
    def __init__(self, 
                 driver: KVSTORE_DRIVER,
                 *,
                 path: Optional[str] = None,
                 context: Optional[Context] = None) -> None:
        super().__init__()
        self.driver = driver.value
        self.path = path
        self.lcontext = context


KvStoreUrl = TypeVar("KvStoreUrl", str)

