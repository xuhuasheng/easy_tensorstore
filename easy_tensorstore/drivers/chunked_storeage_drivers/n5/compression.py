

from abc import ABCMeta
from typing import Literal, Optional
from easy_tensorstore.json_base import JsonBase


class N5Compression(JsonBase, metaclass=ABCMeta):
    """https://google.github.io/tensorstore/driver/n5/index.html#json-driver/n5/Compression"""
    def __init__(self, type: str) -> None:
        super().__init__()
        self.type = type


class N5CompressionRaw(N5Compression):
    def __init__(self) -> None:
        super().__init__(type="raw")


class N5CompressionGzip(N5Compression):
    def __init__(self, 
                 level: int = -1,
                 useZlib: bool = False) -> None:
        super().__init__(type="gzip")
        self.level = level
        self.useZlib = useZlib

class N5CompressionBzip2(N5Compression):
    def __init__(self, 
                 blockSize: int = 9) -> None:
        super().__init__(type="bzio2")
        self.blockSize = blockSize


class N5CompressionXz(N5Compression):
    def __init__(self, 
                 preset : int = 6) -> None:
        super().__init__(type="xz")
        self.preset = preset


class N5CompressionBlosc(N5Compression):
    def __init__(self, 
                 cname: Literal["blosclz", "lz4", "lz4hc", "snappy", "zlib", "zstd"] = "blosclz",
                 clevel: int = 9,
                 shuffle: int = 0,
                 ) -> None:
        super().__init__(type="blosc")
        self.cname = cname 
        self.clevel = clevel
        self.shuffle = shuffle
