
from typing import Literal, Optional, Union

from easy_ts.constant import TS_DRIVER
from easy_ts.context_fx import Context, ContextResource
from easy_ts.index_space import IndexTransform
from easy_ts.kv_storage_layer.kvstore import KvStore
from easy_ts.schema import Schema

from .single_file_driver import SingleFileDriver


class AvifDriver(SingleFileDriver):
    """The avif driver specifies a TensorStore backed by an avif image file. 
    The read volume is indexed by “height” (y), “width” (x), “channel”.
    The avif driver supports between 1 and 4 channel AVIF images. While AVIF 
    images are encoded in YUV planes with varying bit representations, the 
    avif driver converts them, regardless of their encoded depth, to an 
    8-bit Grey/GreyA/RGB/RGBA equivalent image.
    https://google.github.io/tensorstore/driver/image/avif/index.html#avif-driver
    Args:
        https://google.github.io/tensorstore/driver/image/avif/index.html#json-driver/avif
    Examples:
        >>> {"driver": "avif", "kvstore": "gs://my-bucket/path-to-image.avif"}
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
                 quantizer: str = "0",
                 speed: str = "6") -> None:
        super().__init__(driver=TS_DRIVER.avif)
        self.kvstore = kvstore
        self.context = context
        self.dtype = dtype
        self.rank = rank
        self.transform = transform
        self.schema = schema
        self.cache_pool = cache_pool
        self.data_copy_concurrency = data_copy_concurrency
        self.quantizer = quantizer
        self.speed = speed