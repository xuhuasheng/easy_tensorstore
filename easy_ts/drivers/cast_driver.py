"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 16:39:35
LastEditTime : 2024-01-08 15:50:37
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import Optional

import tensorstore as ts

from easy_ts.constant import TS_DRIVER
from easy_ts.context_fx import Context
from easy_ts.index_space import IndexTransform
from easy_ts.schema import Schema

from .spec_base import TsSpecBase


class CastDriver(TsSpecBase):
    """Virtual read/write view that performs element-wise data type conversion.
     - Reading is supported if the base TensorStore supports reading and 
     conversion from the base data type to the view data type is supported.

     - Writing is supported if the base TensorStore supports writing 
     and conversion from the view data type to the base data type is supported.
    Args:
        https://google.github.io/tensorstore/driver/cast/index.html#json-driver/cast
    Examples:
        >>> {
        >>>     "driver": "cast",
        >>>     "dtype": "int32",
        >>>     "base": {"driver": "zarr", "kvstore": {"driver": "gcs", "bucket": "my-bucket"}}
        >>> }
    """
    def __init__(self, 
                 driver: TS_DRIVER, 
                 dtype: ts.dtype, 
                 base: TsSpecBase,
                 *,
                 context: Optional[Context] = None,
                 rank: Optional[int] = None,
                 transform: Optional[IndexTransform] = None,
                 schema: Optional[Schema] = None,
                 ) -> None:
        super().__init__(driver)
        self.dtype = dtype
        self.base = base
        self.context =context
        self.rank = rank
        self.transform = transform
        self.schema = schema
        