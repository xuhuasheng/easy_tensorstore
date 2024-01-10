"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 15:36:25
LastEditTime : 2024-01-05 15:38:20
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
from enum import Enum


class TS_DRIVER(Enum):
    cast = 'cast'
    downsample = 'downsample'
    array = 'array'
    stack = 'stack'
    # single file drivers
    json = 'json'
    avif = 'avif'
    bmp = 'bmp'
    jpeg = 'jpeg'
    png = 'png'
    tiff = 'tiff'
    webp = 'webp'
    # chunked storage drivers
    zarr = 'zarr'
    zarr3 = 'zarr3'
    n5 = 'n5'
    neuroglancer_precomputed = 'neuroglancer_precomputed'


class KVSTORE_DRIVER(Enum):
    file = 'file'
    gcs = 'gcs'
    http = 'http'
    memory = 'memory'
    neuroglancer_uint64_sharded = 'neuroglancer_uint64_sharded'
    ocdbt = 'ocdbt'
    s3 = 's3'
    zarr_sharding_indexed = 'zarr_sharding_indexed'
    zip = 'zip'


class DOWNSAMPLE_METHOD(Enum):
    stride = "stride"
    median = "median"
    mode = "mode"
    mean = "mean"
    min = "min"
    max = "max"