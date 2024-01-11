"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 17:03:45
LastEditTime : 2024-01-08 10:58:54
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from abc import ABCMeta

from easy_tensorstore.constant import TS_DRIVER

from ..spec_base import TsSpecBase


class SingleFileDriver(TsSpecBase, metaclass=ABCMeta):
    def __init__(self, driver: TS_DRIVER) -> None:
        super().__init__(driver)