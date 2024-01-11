from typing import Optional, Union

from easy_tensorstore.constant import KVSTORE_DRIVER
from easy_tensorstore.context_fx import Context, ContextResource

from .kvstore import KvStore, KvStoreUrl


class ZipKvStore(KvStore):
    """https://google.github.io/tensorstore/kvstore/zip/index.html#zip-key-value-store-driver
    Args:
        https://google.github.io/tensorstore/kvstore/zip/index.html#json-kvstore/zip
    Examples:
        >>>    { 
        >>>         "driver": "zip",
        >>>         "kvstore": "gs://my-bucket/path/to/file.zip"
        >>>     }
    """
    def __init__(self,
                 kvstore: Union[KvStore, KvStoreUrl],
                 *, 
                 path: Optional[str] = None, 
                 context: Optional[Context] = None,
                 cache_pool: Union[ContextResource, str] = "cache_pool",
                 data_copy_concurrency: Union[ContextResource, str] = "data_copy_concurrency",) -> None:
        super().__init__(KVSTORE_DRIVER.zip)
        self.kvstore = kvstore
        self.path = path
        self.context = context
        self.cache_pool = cache_pool
        self.data_copy_concurrency = data_copy_concurrency