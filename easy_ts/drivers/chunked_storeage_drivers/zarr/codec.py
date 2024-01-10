"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 10:51:04
LastEditTime : 2024-01-09 11:04:31
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from typing import Optional

from easy_ts.constant import TS_DRIVER
from easy_ts.schema import Codec

from .compressors import Compressor


class ZarrCodec(Codec):
    """https://google.github.io/tensorstore/driver/zarr/index.html#json-driver/zarr/Codec"""
    def __init__(self,
                 compressor: Optional[Compressor] = None,
                 filters = None) -> None:
        super().__init__(driver=TS_DRIVER.zarr)
        self.compressor = compressor
        self.filters = filters