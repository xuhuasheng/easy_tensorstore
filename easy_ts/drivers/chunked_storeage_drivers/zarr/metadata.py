"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 10:52:00
LastEditTime : 2024-01-09 11:04:20
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import List, Literal, Optional

import tensorstore as ts

from easy_ts.json_base import JsonBase

from .compressors import Compressor


class ZarrMetadata(JsonBase):
    """Zarr array metadata.
    Specifies constraints on the metadata, exactly as in the .
    zarray metadata file, except that all members are optional. 
    When creating a new array, the new metadata is obtained by 
    combining these metadata constraints with any Schema constraints.
    https://google.github.io/tensorstore/driver/zarr/index.html#json-driver/zarr.metadata"""
    def __init__(self,
                zarr_format = 2,
                shape: Optional[List[int]] = None,
                chunks: Optional[List[int]] = None,
                dtype: Optional[ts.dtype] = None,
                fill_value: Optional[int] = None,
                order: Literal["C", "F"] = "C",
                compressor: Optional[Compressor] = None,
                filters=None,
                dimension_separator: Literal[".", "/"] = ".",
                ) -> None:
        super().__init__()
        self.zarr_format = zarr_format
        self.shape = shape
        self.chunks = chunks
        self.dtype = dtype
        self.fill_value = fill_value
        self.order = order
        self.compressor = compressor
        self.filters = filters
        self.dimension_separator = dimension_separator