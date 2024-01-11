"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-08 17:36:15
LastEditTime : 2024-01-09 10:50:05
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import List, Literal, Optional, TypeVar, Union

from easy_tensorstore.json_base import JsonBase

from .chunk_key_encoding import ChunkKeyEncoding
from .codec import Zarr3SingleCodec


class Zarr3Metadata(JsonBase):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Metadata"""

    Zarr3DataType = TypeVar("Zarr3DataType", Literal["bool" , "int4" , "int8" , "uint8" ,
                                                 "int16", "uint16", "int32", "uint32", 
                                                 "int64", "uint64", "float16", "bfloat16", 
                                                 "float32", "float64", "complex64", "complex128"])
    CodecChain = TypeVar("CodecChain", List[Union[str, Zarr3SingleCodec]])
    
    class ChunkGrid(JsonBase):
        """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Metadata.chunk_grid"""
        class Configuration(JsonBase):
            """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Metadata.chunk_grid.configuration"""
            def __init__(self, chunk_shape: Optional[List[int]]=None) -> None:
                super().__init__()
                self.chunk_shape = chunk_shape

        def __init__(self,
                     name="regular",
                     configuration: Optional[Configuration]=None) -> None:
            super().__init__()
            self.name = name
            self.configuration = configuration

    class Attributes(JsonBase):
        def __init__(self, dimension_units: Optional[List]) -> None:
            super().__init__()
            self.dimension_units = dimension_units
    
    def __init__(self,
                 zarr_format = 3,
                 node_type = "array",
                 shape: Optional[List[int]] = None,
                 data_type: Optional[Zarr3DataType] = None,
                 chunk_grid: Optional[ChunkGrid] = None,
                 chunk_key_encoding : Optional[ChunkKeyEncoding] = None,
                 fill_value: Optional[int] = None,
                 codecs: Optional[CodecChain] = None,
                 attributes : Optional[Attributes] = None,
                 dimension_names : Optional[List[str]] = None,
                 ) -> None:
        super().__init__()
        self.zarr_format = zarr_format
        self.node_type = node_type
        self.shape = shape
        self.data_type = data_type
        self.chunk_grid = chunk_grid
        self.chunk_key_encoding = chunk_key_encoding
        self.fill_value = fill_value
        self.codecs = codecs
        self.attributes = attributes
        self.dimension_names = dimension_names