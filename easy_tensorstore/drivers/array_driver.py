"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 16:58:59
LastEditTime : 2024-01-08 15:55:33
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from typing import Optional, Sequence

import tensorstore as ts

from easy_tensorstore.constant import TS_DRIVER
from easy_tensorstore.context_fx import Context, ContextResource
from easy_tensorstore.index_space import IndexTransform
from easy_tensorstore.schema import Schema

from .spec_base import TsSpecBase


class ArrayDriver(TsSpecBase):
    """The array driver specifies a TensorStore backed by a contiguous in-memory array.
    When specified via JSON, this driver is useful for specifying small, constant arrays.
    When used from the C++ or Python API, this driver adapts an existing in-memory array 
    for use as a TensorStore.
    Args:
        https://google.github.io/tensorstore/driver/array/index.html#json-driver/array
    Examples:
    >>> {"driver": "array", "array": [[1, 2, 3], [4, 5, 6]], "dtype": "int32"}
    """
    def __init__(self, 
                 driver: TS_DRIVER,
                 dtype: ts.dtype, 
                 array: Sequence,
                 *,
                 context: Optional[Context] = None,
                 rank: Optional[int] = None,
                 transform: Optional[IndexTransform] = None,
                 schema: Optional[Schema] = None,
                 data_copy_concurrency: ContextResource = "data_copy_concurrency") -> None:
        super().__init__(driver)
        self.dtype = dtype
        self.array = array
        self.context =context
        self.rank = rank
        self.transform = transform
        self.schema = schema
        self.data_copy_concurrency = data_copy_concurrency