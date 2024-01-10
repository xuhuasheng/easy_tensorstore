

import tensorstore as ts
from typing import Sequence, Optional, List
from easy_ts.constant import KVSTORE_DRIVER, TS_DRIVER
from easy_ts.context_fx import Context
from easy_ts.drivers.spec_base import TsSpecBase
from easy_ts.index_space import IndexDomain
from easy_ts.kv_storage_layer.kvstore import KvStore
from easy_ts.schema import ChunkLayout, Codec, Schema


    
def ts_open(spec: TsSpecBase, 
            *, 
            read: Optional[bool]= None, 
            write: Optional[bool] = None, 
            open: Optional[bool] = None, 
            create: Optional[bool] = None, 
            delete_existing: Optional[bool] = None, 
            assume_metadata: Optional[bool] = None, 
            assume_cached_metadata: Optional[bool] = None, 
            context: Optional[Context] = None, 
            kvstore: Optional[KvStore] = None, 
            rank: Optional[int] = None, 
            dtype: Optional[ts.dtype] = None, 
            domain: Optional[IndexDomain] = None, 
            shape: Optional[Sequence[int]] = None, 
            chunk_layout: Optional[ChunkLayout] = None, 
            codec: Optional[Codec] = None, 
            fill_value: Optional[List] = None, 
            dimension_units: Optional[Sequence] = None, 
            schema: Optional[Schema] = None) -> ts.Future:
    return ts.open(
            spec,
            read,
            write,
            open,
            create,
            delete_existing,
            assume_metadata,
            assume_cached_metadata,
            context,
            kvstore,
            rank,
            dtype,
            domain,
            shape, 
            chunk_layout,
            codec, 
            fill_value, 
            dimension_units,
            schema,
    )