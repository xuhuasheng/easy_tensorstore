
from typing import Literal, Optional, Union

from easy_ts.constant import TS_DRIVER
from easy_ts.context_fx import Context, ContextResource
from easy_ts.index_space import IndexTransform
from easy_ts.kv_storage_layer.kvstore import KvStore, KvStoreUrl
from easy_ts.schema import Schema

from ..chunked_driver import ChunkedDriver
from .metadata import MultiscaleMetadata, ScaleMetadata


class NeuroglancerPrecomputedDriver(ChunkedDriver):
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
                 scale_index : Optional[int] = None,
                 multiscale_metadata : Optional[MultiscaleMetadata] = None,
                 scale_metadata : Optional[ScaleMetadata] = None,
                 ) -> None:
        super().__init__(TS_DRIVER.neuroglancer_precomputed, kvstore)
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
        self.scale_index = scale_index
        self.multiscale_metadata = multiscale_metadata
        self.scale_metadata = scale_metadata