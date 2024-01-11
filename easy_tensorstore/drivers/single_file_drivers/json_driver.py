
from typing import Literal, Optional, Union

from easy_tensorstore.constant import TS_DRIVER
from easy_tensorstore.context_fx import Context, ContextResource
from easy_tensorstore.index_space import IndexTransform
from easy_tensorstore.kv_storage_layer.kvstore import KvStore, KvStoreUrl
from easy_tensorstore.schema import Schema

from .single_file_driver import SingleFileDriver


class JsonDriver(SingleFileDriver):
    """The json driver provides read/write access to JSON values stored in 
    any supported Key-Value Storage Layer. JSON values are accessed as rank-0 
    arrays with "json" data type.
    https://google.github.io/tensorstore/driver/json/index.html#json-driver
    Args:
        https://google.github.io/tensorstore/driver/json/index.html#json-driver/json
    Examples:
    >>>  {
    >>>    "driver": "json",
    >>>    "kvstore": {"driver": "gcs", "bucket": "my-bucket"},
    >>>    "path": "path/to/attributes.json",
    >>>    "json_pointer": "/a/2/b"
    >>>  }
    """
    def __init__(self, 
                 kvstore: Union[KvStore, KvStoreUrl] = None,
                 *,
                 context: Optional[Context] = None,
                 dtype: Literal['json'] = 'json',
                 rank: int = 0,
                 transform: Optional[IndexTransform] = None,
                 schema: Optional[Schema] = None,
                 path: Optional[str] = None,
                 cache_pool: Union[ContextResource, str] = "cache_pool",
                 data_copy_concurrency: Union[ContextResource, str] = "data_copy_concurrency",
                 recheck_cached_data: Union[bool, Literal["open"], int] = "open",
                 json_pointer: str = "") -> None:
        super().__init__(driver=TS_DRIVER.json)
        self.kvstore = kvstore
        self.context = context
        self.dtype = dtype
        self.rank = rank
        self.transform = transform
        self.schema = schema
        self.path = path
        self.cache_pool = cache_pool
        self.data_copy_concurrency = data_copy_concurrency
        self.recheck_cached_data = recheck_cached_data
        self.json_pointer = json_pointer