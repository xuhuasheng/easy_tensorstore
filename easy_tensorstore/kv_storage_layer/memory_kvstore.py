"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 15:43:32
LastEditTime : 2024-01-10 11:05:36
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from typing import Optional

from easy_tensorstore.constant import KVSTORE_DRIVER
from easy_tensorstore.context_fx import Context
from easy_tensorstore.json_base import JsonBase

from .kvstore import KvStore


class MemoryKvStore(KvStore):
    """https://google.github.io/tensorstore/kvstore/memory/index.html#memory-key-value-store-driver
    Args:
        https://google.github.io/tensorstore/kvstore/memory/index.html#json-kvstore/memory"""
    def __init__(self, 
                 *,
                 path: Optional[str] = None,
                 context: Optional[Context] = None,
                 memory_key_value_store: Optional[JsonBase] = None,
                 atomic: bool = True,
                 ) -> None:
        super().__init__(KVSTORE_DRIVER.memory)
        self.path = path
        self.context = context
        self.memory_key_value_store = memory_key_value_store
        self.atomic = atomic