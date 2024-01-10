"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 10:47:18
LastEditTime : 2024-01-09 11:04:08
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import Literal, Optional
from easy_ts.json_base import JsonBase


class Compressor(JsonBase):
    def __init__(self, id: str) -> None:
        self.id = id

class BloscCompressor(Compressor):
    """https://google.github.io/tensorstore/driver/zarr/index.html#json-driver/zarr/Compressor/blosc"""
    def __init__(self,
                 cname: Literal["blosclz", "lz4", "lz4hc", "snappy", "zlib", "zstd"] = "lz4",
                 clevel: int = 5,
                 shuffle: int = -1,
                 blocksize: Optional[int] = None) -> None:
        super().__init__(id="blosc")
        assert cname in ("blosclz", "lz4", "lz4hc", "snappy", "zlib", "zstd")
        self.cname = cname
        assert 0 <= clevel <= 9
        self.clevel = clevel
        assert shuffle in (-1, 0, 1, 2)
        self.shuffle = shuffle
        if blocksize is not None:
            assert blocksize >= 0
        self.blocksize = blocksize

class Bz2Compressor(Compressor):
    """https://google.github.io/tensorstore/driver/zarr/index.html#json-driver/zarr/Compressor/bz2"""
    def __init__(self,
                 level: int = 1) -> None:
        super().__init__(id="bz2")
        assert 1 <= level <= 9
        self.level = level

class ZlibCompressor(Compressor):
    """https://google.github.io/tensorstore/driver/zarr/index.html#json-driver/zarr/Compressor/zlib"""
    def __init__(self, id: Literal["zlib", "gzip"], level: Optional[int] = 1) -> None:
        super().__init__(id)
        assert 0 <= level <= 9
        self.level = level

class ZstdCompressor(Compressor):
    """https://google.github.io/tensorstore/driver/zarr/index.html#json-driver/zarr/Compressor/zstd"""
    def __init__(self,
                 level: int = 1) -> None:
        super().__init__(id="zstd")
        assert -131072 <= level <= 22
        self.level = level