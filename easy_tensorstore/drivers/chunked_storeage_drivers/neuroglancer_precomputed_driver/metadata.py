"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 11:29:04
LastEditTime : 2024-01-09 11:43:16
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import List, Literal, Optional, Union
from easy_tensorstore.json_base import JsonBase
from easy_tensorstore.kv_storage_layer.neuroglancer_uint64_sharded_kvstore import NgUint64SharedShardingSpec


class MultiscaleMetadata(JsonBase):
    def __init__(self,
                 type: Optional[Literal["image", "segmentation"]] = None,
                 data_type: Optional[Literal["uint8", "uint16", "uint32", "uint64", "float32"]] = None,
                 num_channels : int = None,
                 ) -> None:
        super().__init__()
        self.type = type
        self.data_type = data_type
        self.num_channels = num_channels


class ScaleMetadata(JsonBase):
    def __init__(self,
                 key: Optional[str] = None,
                 size: Optional[List[int]] = None,
                 voxel_offset : Optional[List[int]] = None,
                 chunk_size : Optional[List[int]] = None,
                 resolution : Optional[List[int]] = None,
                 encoding : Optional[Literal["raw", "jpeg", "compressed_segmentation"]] = None,
                 jpeg_quality: int = 75,
                 compressed_segmentation_block_size : Optional[List[int]] = None,
                 sharding: Union[NgUint64SharedShardingSpec, str] = "null") -> None:
        super().__init__()
        self.key = key
        self.size = size
        self.voxel_offset = voxel_offset
        self.chunk_size = chunk_size
        self.resolution = resolution
        self.encoding = encoding
        self.jpeg_quality = jpeg_quality
        self.compressed_segmentation_block_size = compressed_segmentation_block_size
        self.sharding = sharding

