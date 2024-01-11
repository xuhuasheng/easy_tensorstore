"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-08 16:46:19
LastEditTime : 2024-01-08 16:48:14
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import Literal, Optional, Union

from easy_tensorstore.constant import TS_DRIVER
from easy_tensorstore.context_fx import Context, ContextResource
from easy_tensorstore.index_space import IndexTransform
from easy_tensorstore.kv_storage_layer.kvstore import KvStore
from easy_tensorstore.schema import Schema

from .single_file_driver import SingleFileDriver


class TiffDriver(SingleFileDriver):
    """The tiff driver specifies a TensorStore backed by a TIFF image file. 
    The read volume is indexed by “height” (y), “width” (x), “channel”.
    This driver is currently experimental and only supports a very limited subset of TIFF files.
    https://google.github.io/tensorstore/driver/image/tiff/index.html#tiff-driver
    Args:
        https://google.github.io/tensorstore/driver/image/tiff/index.html#json-driver/tiff
    Examples:
        >>> {"driver": "tiff", "kvstore": "gs://my-bucket/path-to-image.tiff"}
    """
    def __init__(self, 
                 kvstore: KvStore,
                 *,
                 context: Optional[Context] = None,
                 dtype: Literal['uint8'] = 'uint8',
                 rank: int = 0,
                 transform: Optional[IndexTransform] = None,
                 schema: Optional[Schema] = None,
                 cache_pool: Union[ContextResource, str] = "cache_pool",
                 data_copy_concurrency: Union[ContextResource, str] = "data_copy_concurrency",
                 page : Optional[str] = None) -> None:
        super().__init__(driver=TS_DRIVER.tiff)
        self.kvstore = kvstore
        self.context = context
        self.dtype = dtype
        self.rank = rank
        self.transform = transform
        self.schema = schema
        self.cache_pool = cache_pool
        self.data_copy_concurrency = data_copy_concurrency
        self.page = page