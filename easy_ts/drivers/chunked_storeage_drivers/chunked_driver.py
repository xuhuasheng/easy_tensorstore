"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-08 16:52:22
LastEditTime : 2024-01-08 16:56:21
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from abc import ABCMeta
from typing import Union

from easy_ts.constant import TS_DRIVER
from easy_ts.drivers.spec_base import TsSpecBase
from easy_ts.kv_storage_layer.kvstore import KvStore, KvStoreUrl


class ChunkedDriver(TsSpecBase, metaclass=ABCMeta):
    """Common options supported by all chunked storage drivers.
    https://google.github.io/tensorstore/driver/index.html#chunked-storage-drivers
    """
    def __init__(self, 
                 driver: TS_DRIVER, 
                 kvstore: Union[KvStore, KvStoreUrl]) -> None:
        super().__init__(driver)
        self.kvstore = kvstore