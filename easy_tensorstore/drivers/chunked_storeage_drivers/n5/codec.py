"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 10:56:10
LastEditTime : 2024-01-09 11:15:39
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import Optional

from easy_tensorstore.constant import TS_DRIVER
from easy_tensorstore.schema import Codec

from .compression import N5Compression


class N5Codec(Codec):
    def __init__(self, 
                 compression: Optional[N5Compression]) -> None:
        super().__init__(driver=TS_DRIVER.n5)
        self.compression = compression