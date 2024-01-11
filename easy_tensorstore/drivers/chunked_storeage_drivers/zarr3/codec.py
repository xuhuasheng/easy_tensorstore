"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 09:51:00
LastEditTime : 2024-01-09 10:42:48
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from abc import ABCMeta
from typing import List, Literal, Optional, TypeVar, Union

from easy_tensorstore.constant import TS_DRIVER
from easy_tensorstore.json_base import JsonBase
from easy_tensorstore.schema import Codec


class Zarr3SingleCodec(JsonBase, metaclass=ABCMeta):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/SingleCodec"""
    def __init__(self, 
                 name: str, 
                 configuration: Optional[JsonBase] = None) -> None:
        super().__init__()
        self.name = name
        self.configuration = configuration


Zarr3CodecChain = TypeVar("Zarr3CodecChain", List[Union[str, Zarr3SingleCodec]])


class Zarr3CodecTranspose(Zarr3SingleCodec):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Codec/transpose"""
    class Configuration(JsonBase):
        def __init__(self, order: Optional[List[Union[int, Literal["C", "F"]]]]) -> None:
            super().__init__()
            self.order = order

    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        super().__init__(name="transpose", configuration=configuration)


class Zarr3CodecBytes(Zarr3SingleCodec):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Codec/bytes"""
    class Configuration(JsonBase):
        def __init__(self, endian: Optional[Literal["little", "big"]]) -> None:
            super().__init__()
            self.endian = endian 

    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        super().__init__(name="bytes", configuration=configuration)


class Zarr3CodecShardingIndexed(Zarr3SingleCodec):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Codec/sharding_indexed"""
    class Configuration(JsonBase):
        def __init__(self, 
                     chunk_shape: Optional[List[int]] = None,
                     codecs: Optional[Zarr3CodecChain] = None,
                     index_codecs: Optional[Zarr3CodecChain] = None,
                     index_location: Literal["start", "end"] = "end") -> None:
            super().__init__()
            self.chunk_shape = chunk_shape 
            self.codecs = codecs
            self.index_codecs = index_codecs
            self.index_location = index_location

    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        super().__init__(name="sharding_indexed", configuration=configuration)


class Zarr3CodecGzip(Zarr3SingleCodec):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Codec/gzip"""
    class Configuration(JsonBase):
        def __init__(self, 
                     level: Optional[int] = None) -> None:
            super().__init__()
            self.level = level 

    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        super().__init__(name="gzip", configuration=configuration)


class Zarr3CodecBlosc(Zarr3SingleCodec):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Codec/blosc"""
    class Configuration(JsonBase):
        def __init__(self, 
                     cname: Literal["blosclz", "lz4", "lz4hc", "snappy", "zlib", "zstd"] = "lz4",
                     clevel: int = 5,
                     shuffle: Literal["noshuffle", "shuffle", "bitshuffle"] = "noshuffle",
                     typesize: Optional[int] = None,
                     blocksize: int = 0) -> None:
            super().__init__()
            self.cname = cname 
            self.clevel = clevel
            self.shuffle = shuffle
            self.typesize = typesize
            self.blocksize = blocksize

    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        super().__init__(name="blosc", configuration=configuration)


class Zarr3CodecZstd(Zarr3SingleCodec):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Codec/zstd"""
    class Configuration(JsonBase):
        def __init__(self, 
                     level: int = 1,
                     ) -> None:
            super().__init__()
            self.level = level
   
    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        super().__init__(name="zstd", configuration=configuration)


class Zarr3CodecCrc32c(Zarr3SingleCodec):
    """https://google.github.io/tensorstore/driver/zarr3/index.html#json-driver/zarr3/Codec/crc32c"""
   
    def __init__(self) -> None:
        super().__init__(name="crc32c", configuration=None)


class Zarr3Codec(Codec):
    
    def __init__(self, codecs: Optional[Zarr3CodecChain] = None) -> None:
        super().__init__(driver=TS_DRIVER.zarr3)
        self.codecs = codecs

