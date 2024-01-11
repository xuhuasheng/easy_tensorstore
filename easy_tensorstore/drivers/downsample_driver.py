"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 16:55:46
LastEditTime : 2024-01-08 15:52:11
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from typing import Optional, Sequence

from easy_tensorstore.constant import DOWNSAMPLE_METHOD, TS_DRIVER
from easy_tensorstore.context_fx import Context
from easy_tensorstore.index_space import IndexTransform
from easy_tensorstore.schema import Schema

from .spec_base import TsSpecBase


class DownsampleDriver(TsSpecBase):
    """Virtual read-only view that performs downsampling.
    Downsampling is performed on-the-fly to compute exactly 
    the positions of the downsampled view that are read.
    Args:
        https://google.github.io/tensorstore/driver/downsample/index.html#json-driver/downsample
    Examlpes:
    >>> {
    >>>   "driver": "downsample",
    >>>   "downsample_factors": [1, 2, 2],
    >>>   "downsample_method": "mean",
    >>>   "base": {"driver": "zarr", "kvstore": {"driver": "gcs", "bucket": "my-bucket"}}
    >>> }
    """
    def __init__(self, 
                 driver: TS_DRIVER, 
                 base: TsSpecBase,
                 downsample_factors: Sequence,
                 downsample_method: DOWNSAMPLE_METHOD,
                 *,
                 context: Optional[Context] = None,
                 rank: Optional[int] = None,
                 transform: Optional[IndexTransform] = None,
                 schema: Optional[Schema] = None,) -> None:
        super().__init__(driver)
        self.base = base
        self.downsample_factors = downsample_factors
        self.downsample_method = downsample_method
        self.context =context
        self.rank = rank
        self.transform = transform
        self.schema = schema