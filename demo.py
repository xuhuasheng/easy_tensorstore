"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-04 14:09:36
LastEditTime : 2024-01-05 11:08:10
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""
import time

import numpy as np
import skimage.io as skio
import tensorstore as ts
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

img_path = r"e:\AIRCAS\Projects\PCB-Damage-Detection\data\iphone\a\gerberTemp.tiff"

t = time.perf_counter()
img = skio.imread(img_path)
print(f"skio.imread: {time.perf_counter() - t}")

t = time.perf_counter()
data =[[1,2,3], [3,4,5]]
store_future = ts.open(
    {
        'driver': 'array',
        "array": data,
        'dtype': ts.int8,
    },
    create=True,
    delete_existing=True,


)
store = store_future.result()
store[:] = img
print(f"ts.open: {time.perf_counter() - t}")


t = time.perf_counter()
store_future = ts.open(
    {
        'driver': 'n5',
        'kvstore': {
            'driver': 'file',
            'path': 'mmmm'
        }
    },
    open=True
    # dtype=ts.uint8,
    # shape=img.shape,
)
store = store_future.result()
img = store[100:200,...]
print(f"ts.read: {time.perf_counter() - t}")


