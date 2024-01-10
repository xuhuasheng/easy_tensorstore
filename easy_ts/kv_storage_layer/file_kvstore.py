"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 17:39:51
LastEditTime : 2024-01-10 11:09:26
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import Literal, Optional, Union

from easy_ts.constant import KVSTORE_DRIVER
from easy_ts.context_fx import Context, ContextResource

from .kvstore import KvStore


class FileIoConcurrency(ContextResource):
    def __init__(self, 
                 limit: Optional[Union[int, Literal["shared"]]] = "shared") -> None:
        super().__init__()
        self.limit = limit


class FileKvStore(KvStore):
    """https://google.github.io/tensorstore/kvstore/file/index.html#file-key-value-store-driver"""
    def __init__(self, 
                 path: str,
                 *,
                 context: Optional[Context] = None,
                 file_io_concurrency: Optional[FileIoConcurrency] = None,
                 file_io_sync: Optional[bool] = None) -> None:
        super().__init__(KVSTORE_DRIVER.file)
        self.path = path
        self.context = context
        self.file_io_concurrency = file_io_concurrency
        self.file_io_sync = file_io_sync

