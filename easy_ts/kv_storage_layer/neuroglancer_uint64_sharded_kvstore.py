from typing import Literal, Optional, Union

from easy_ts.constant import KVSTORE_DRIVER
from easy_ts.context_fx import Context
from easy_ts.json_base import JsonBase

from .kvstore import KvStore, KvStoreUrl


class NgUint64SharedShardingSpec(JsonBase):
    """https://google.github.io/tensorstore/kvstore/neuroglancer_uint64_sharded/index.html#json-kvstore/neuroglancer_uint64_sharded/ShardingSpec"""
    def __init__(self, 
                preshift_bits: int,
                hash: Literal["identity", "murmurhash3_x86_128"],
                minishard_bits: int,
                shard_bits: int,
                *,
                minishard_index_encoding: Literal["raw", "gzip"] = "raw",
                data_encoding: Literal["raw", "gzip"] = "raw") -> None:
        super().__init__()
        self.type = "neuroglancer_uint64_sharded_v1"
        self.preshift_bits = preshift_bits
        self.hash = hash
        self.minishard_bits = minishard_bits
        self.shard_bits = shard_bits
        self.minishard_index_encoding = minishard_index_encoding
        self.data_encoding = data_encoding
        

class NgUint64SharedKvStore(KvStore):
    """https://google.github.io/tensorstore/kvstore/neuroglancer_uint64_sharded/index.html#neuroglancer-uint64-sharded-key-value-store-driver
    Args:
        https://google.github.io/tensorstore/kvstore/neuroglancer_uint64_sharded/index.html#json-kvstore/neuroglancer_uint64_sharded
    Examples:
        1. Opening with identity hash and 1GB cache
        >>> {
        >>>     "driver": "neuroglancer_uint64_sharded",
        >>>     "kvstore": "gs://my-bucket/path/to/sharded/data/",
        >>>     "metadata": {
        >>>         "@type": "neuroglancer_uint64_sharded_v1",
        >>>         "hash": "identity",
        >>>         "preshift_bits": 1,
        >>>         "minishard_bits": 3,
        >>>         "shard_bits": 3,
        >>>         "data_encoding": "raw",
        >>>         "minishard_index_encoding": "gzip",
        >>>     },
        >>>     "context": {
        >>>         "cache_pool": {"total_bytes_limit": 1000000000}
        >>>     }
        >>> }
        2. Opening with murmurhash3_x86_128 hash and 1GB cache
        >>> {
        >>>     "driver": "neuroglancer_uint64_sharded",
        >>>     "kvstore": "gs://my-bucket/path/to/sharded/data/",
        >>>     "metadata": {
        >>>         "@type": "neuroglancer_uint64_sharded_v1",
        >>>         "hash": "murmurhash3_x86_128",
        >>>         "preshift_bits": 0,
        >>>         "minishard_bits": 3,
        >>>         "shard_bits": 3,
        >>>         "data_encoding": "raw",
        >>>         "minishard_index_encoding": "gzip",
        >>>     },
        >>>     "context": {
        >>>         "cache_pool": {"total_bytes_limit": 1000000000}
        >>>     }
        >>> }
    """
    def __init__(self, 
                 kvstore: Union[KvStore, KvStoreUrl],
                 metadata: NgUint64SharedShardingSpec,
                 *,
                 path: Optional[str] = None,
                 context: Optional[Context] = None,
                 memory_key_value_store: Optional[JsonBase] = None,
                 atomic: bool = True,
                 ) -> None:
        super().__init__(KVSTORE_DRIVER.neuroglancer_uint64_sharded)
        self.kvstore = kvstore
        self.metadata = metadata
        self.path = path
        self.context = context
        self.memory_key_value_store = memory_key_value_store
        self.atomic = atomic