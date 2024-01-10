"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 17:00:59
LastEditTime : 2024-01-08 15:59:22
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from typing import List, Optional

from easy_ts.constant import TS_DRIVER
from easy_ts.context_fx import Context, ContextResource
from easy_ts.index_space import IndexTransform
from easy_ts.schema import Schema

from .spec_base import TsSpecBase


class StackDriver(TsSpecBase):
    """The stack driver specifies a TensorStore virtually overlays a 
    sequence of TensorStore layers within a common domain.
    https://google.github.io/tensorstore/driver/stack/index.html#stack-driver
    Args:
        https://google.github.io/tensorstore/driver/stack/index.html#json-driver/stack
    Examples:
    >>> {
    >>>  "driver": "stack",
    >>>  "layers": [ {"driver": "array", "array": [1, 2, 3], "dtype": "int32"},
    >>>      {
    >>>      "driver": "array",
    >>>      "array": [4, 5, 6],
    >>>      "dtype": "int32",
    >>>      "transform": {
    >>>          "input_inclusive_min": 3,
    >>>          "output": {"input_dimension": 0, "offset": -3}
    >>>      }
    >>>      }]
    >>>  }
    """
    def __init__(self, 
                 driver: TS_DRIVER,
                 layers: List[TsSpecBase], 
                 *,
                 context: Optional[Context] = None,
                 rank: Optional[int] = None,
                 transform: Optional[IndexTransform] = None,
                 schema: Optional[Schema] = None,
                 data_copy_concurrency: ContextResource = "data_copy_concurrency") -> None:
        super().__init__(driver)
        self.layers = layers
        self.context =context
        self.rank = rank
        self.transform = transform
        self.schema = schema
        self.data_copy_concurrency = data_copy_concurrency