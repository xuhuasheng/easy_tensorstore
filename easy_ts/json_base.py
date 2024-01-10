"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 15:44:11
LastEditTime : 2024-01-08 15:07:19
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import Dict


class JsonBase:
    def __init__(self) -> None:
        self._dict = dict()

    def json(self) -> Dict:
        for k, v in self.__dict__.items():
            if k.startswith('_'):
                continue
            if v is None:
                continue
            if v == 'null':
                v = None
            if isinstance(v, JsonBase):
                self._dict.update({k: v.json()})
            self._dict.update({k: v})
        return self._dict