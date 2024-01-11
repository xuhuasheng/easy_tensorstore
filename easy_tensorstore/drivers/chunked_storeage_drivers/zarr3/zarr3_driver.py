
"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-08 16:56:35
LastEditTime : 2024-01-09 09:32:24
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from typing import Literal, Optional, Union

from easy_tensorstore.constant import TS_DRIVER
from easy_tensorstore.context_fx import Context, ContextResource
from easy_tensorstore.index_space import IndexTransform
from easy_tensorstore.kv_storage_layer.kvstore import KvStore, KvStoreUrl
from easy_tensorstore.schema import Schema

from ..chunked_driver import ChunkedDriver
from .metadata import Zarr3Metadata


class Zarr3Driver(ChunkedDriver):
    """Zarr v3 is a chunked array storage format.
    The zarr3 driver provides access to Zarr v3-format arrays backed by any supported Key-Value
      Storage Layer. It supports reading, writing, creating new arrays, and resizing arrays.
        https://google.github.io/tensorstore/driver/zarr3/index.html#zarr3-driver
    Args:
        https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3
    Examples:
    >>> {
    >>>     "driver": "zarr3",
    >>>     "kvstore": {"driver": "gcs", "bucket": "my-bucket", "path": "path/to/array/"},
    >>>     "metadata": {
    >>>         "shape": [1000, 1000],
    >>>         "chunk_grid": {"name": "regular", "configuration": {"chunk_shape": [100, 100]}},
    >>>         "chunk_key_encoding": {"name": "default"},
    >>>         "codecs": [{"name": "blosc", "configuration": {"cname": "lz4", "clevel": 5}}],
    >>>         "data_type": "int4"
    >>>     }
    >>> }
    """
    def __init__(self, 
                 kvstore: Union[KvStore, KvStoreUrl],
                 *,
                 context: Optional[Context] = None,
                 dtype: Literal['uint8'] = 'uint8',
                 rank: int = 0,
                 transform: Optional[IndexTransform] = None,
                 schema: Optional[Schema] = None,
                 path: str = "",
                 open: bool = False,
                 create: bool = False,
                 delete_existing: bool = False,
                 assume_metadata: bool = False,
                 assume_cached_metadata: bool = False,
                 cache_pool: Union[ContextResource, str] = "cache_pool",
                 data_copy_concurrency: Union[ContextResource, str] = "data_copy_concurrency",
                 recheck_cached_metadata: Union[bool, Literal["open"], int] = "open",
                 recheck_cached_data: Union[bool, Literal["open"], int] = True,
                 field: Optional[str] = None,
                 metadata: Optional[Zarr3Metadata] = None,
                 ) -> None:
        super().__init__(TS_DRIVER.zarr3, kvstore)
        self.context = context
        self.dtype = dtype
        self.rank = rank
        self.transform = transform
        self.schema = schema
        self.path = path
        self.open = open
        self.create = create
        self.delete_existing = delete_existing
        self.assume_metadata = assume_metadata
        self.assume_cached_metadata = assume_cached_metadata
        self.cache_pool = cache_pool
        self.data_copy_concurrency = data_copy_concurrency
        self.recheck_cached_metadata = recheck_cached_metadata
        self.recheck_cached_data = recheck_cached_data
        self.field = field
        self.metadata = metadata
