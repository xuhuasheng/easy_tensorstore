"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-10 10:29:17
LastEditTime : 2024-01-10 10:56:12
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""


from typing import Literal, Optional, Union

from easy_tensorstore.constant import KVSTORE_DRIVER
from easy_tensorstore.context_fx import Context, ContextResource
from easy_tensorstore.drivers.chunked_storeage_drivers.zarr3.codec import Zarr3CodecChain

from .kvstore import KvStore, KvStoreUrl
from .neuroglancer_uint64_sharded_kvstore import NgUint64SharedShardingSpec


class ZarrShardingIndexedKvStore(KvStore):
    """https://google.github.io/tensorstore/kvstore/zarr3_sharding_indexed/index.html#zarr-sharding-indexed-key-value-store-driver
    Args:
        https://google.github.io/tensorstore/kvstore/zarr3_sharding_indexed/index.html#json-kvstore/zarr_sharding_indexed
    Examples:
        >>> {
        >>>     "driver": "zarr_sharding_indexed",
        >>>     "kvstore": "gs://my-bucket/path/to/sharded/data",
        >>>     "grid_shape": [32, 128],
        >>>     "index_codecs" [
        >>>         {"name": "bytes", "configuration": {"endian": "little"}},
        >>>         {"name": "crc32c"}
        >>>     ],
        >>>     "context": {
        >>>         "cache_pool": {"total_bytes_limit": 1000000000}
        >>>     }
        >>> }
    """
    def __init__(self,
                 kvstore: Union[KvStore, KvStoreUrl],
                 grid_shape: NgUint64SharedShardingSpec,
                 index_codecs: Zarr3CodecChain,
                 *, 
                 path: Optional[str] = None, 
                 context: Optional[Context] = None,
                 index_location: Literal["start", "end"] = "end",
                 cache_pool: Union[ContextResource, str] = "cache_pool",
                 data_copy_concurrency: Union[ContextResource, str] = "data_copy_concurrency",) -> None:
        super().__init__(KVSTORE_DRIVER.zarr_sharding_indexed)
        self.kvstore = kvstore
        self.grid_shape = grid_shape
        self.index_codecs = index_codecs
        self.path = path
        self.context = context
        self.index_location = index_location
        self.cache_pool = cache_pool
        self.data_copy_concurrency = data_copy_concurrency