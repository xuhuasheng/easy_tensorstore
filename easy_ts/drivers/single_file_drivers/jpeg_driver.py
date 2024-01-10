
from typing import Literal, Optional, Union

from easy_ts.constant import TS_DRIVER
from easy_ts.context_fx import Context, ContextResource
from easy_ts.index_space import IndexTransform
from easy_ts.kv_storage_layer.kvstore import KvStore
from easy_ts.schema import Schema

from .single_file_driver import SingleFileDriver


class JpegDriver(SingleFileDriver):
    """The jpeg driver specifies a TensorStore backed by a jpeg. 
    The read volume is indexed by “height” (y), “width” (x), “channel”.
    https://google.github.io/tensorstore/driver/image/jpeg/index.html#jpeg-driver
    Args:
        https://google.github.io/tensorstore/driver/image/jpeg/index.html#json-driver/jpeg
    Examples:
        >>> {"driver": "jpeg", "kvstore": "gs://my-bucket/path-to-image.jpg"}
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
                 quality : int = 75) -> None:
        super().__init__(driver=TS_DRIVER.jpeg)
        self.kvstore = kvstore
        self.context = context
        self.dtype = dtype
        self.rank = rank
        self.transform = transform
        self.schema = schema
        self.cache_pool = cache_pool
        self.data_copy_concurrency = data_copy_concurrency
        self.quality = quality