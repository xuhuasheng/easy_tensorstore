"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 15:59:47
LastEditTime : 2024-01-10 10:58:12
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""


from typing import Literal, Optional, Union

from easy_tensorstore.constant import KVSTORE_DRIVER
from easy_tensorstore.context_fx import Context, ContextResource
from easy_tensorstore.json_base import JsonBase

from .kvstore import KvStore, KvStoreUrl


class OcdbtCompressionZstd(JsonBase):
    def __init__(self, level: Optional[int] = None) -> None:
        super().__init__()
        self.id = "zstd"
        self.level = level

class Config(JsonBase):
    def __init__(self,
                 uuid: Optional[str] = None,
                 manifest_kind: Optional[Literal["single", "numbered"]] = None,
                 max_inline_value_bytes: int = 100,
                 max_decoded_node_bytes: int = 83951616,
                 version_tree_arity_log2: int = 4,
                 compression: Union[OcdbtCompressionZstd, Literal["null"]] = OcdbtCompressionZstd(level=0),
                 ) -> None:
        super().__init__()
        self.uuid = uuid
        self.manifest_kind = manifest_kind
        self.max_inline_value_bytes = max_inline_value_bytes
        self.max_decoded_node_bytes = max_decoded_node_bytes
        self.version_tree_arity_log2 = version_tree_arity_log2
        self.compression = compression

class OcdbtCoordinator(ContextResource):
    def __init__(self, 
                 address: Optional[str] = None,
                 lease_duration: str = "10s") -> None:
        super().__init__() 
        self.address = address
        self.lease_duration = lease_duration


class OcdbtKvstore(KvStore):
    """https://google.github.io/tensorstore/kvstore/ocdbt/index.html#ocdbt-key-value-store-driver
    Args:
        https://google.github.io/tensorstore/kvstore/ocdbt/index.html#json-kvstore/ocdbt"""
    def __init__(self, 
                 kvstore: Union[KvStore, KvStoreUrl],
                 *,
                 path: Optional[str] = None,
                 context: Optional[Context] = None,
                 coordinator: Optional[OcdbtCoordinator],
                 config: Optional[Config] = None,
                 cache_pool: Union[ContextResource, str] = "cache_pool",
                 data_copy_concurrency: Union[ContextResource, str] = "data_copy_concurrency",) -> None:
        super().__init__(KVSTORE_DRIVER.ocdbt)
        self.kvstore = kvstore
        self.path = path
        self.context = context
        self.coordinator = coordinator
        self.config = config
        self.cache_pool = cache_pool
        self.data_copy_concurrency = data_copy_concurrency


