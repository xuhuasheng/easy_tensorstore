"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-08 16:56:35
LastEditTime : 2024-01-09 09:32:24
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from abc import ABCMeta
from typing import Literal, Optional

from easy_ts.json_base import JsonBase


class ChunkKeyEncoding(JsonBase, metaclass=ABCMeta):
    """The position of each chunk is encoded as a key according 
    to the chunk_key_encoding specified in the metadata.
    https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/ChunkKeyEncoding"""
    def __init__(self, 
                 name: Optional[str] = None, 
                 configuration: Optional[JsonBase] = None) -> None:
        super().__init__()
        self.name = name
        self.configuration = configuration

class ChunkKeyEncodingDefault(ChunkKeyEncoding):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/ChunkKeyEncoding.default"""
    class Configuration(JsonBase):
        def __init__(self, separator: Literal["/", "."] = "/") -> None:
            super().__init__()
            self.separator = separator

    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        super().__init__(name="default", configuration=configuration)

class ChunkKeyEncodingV2(ChunkKeyEncoding):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/ChunkKeyEncoding.v2"""
    class Configuration(JsonBase):
        def __init__(self, separator: Literal["/", "."] = ".") -> None:
            super().__init__()
            self.separator = separator

    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        super().__init__(name="v2", configuration=configuration)