"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-08 15:08:15
LastEditTime : 2024-01-08 15:33:00
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

"""TensorStore defines an index space as an n-dimensional space, where n
is the rank of the space and each index is an integer in the closed interval [-(2^62)-2, +(2^62-2)]. 
The special values ±(2^62-1) are not valid indices but represent bounds of +∞.

TensorStore currently supports ranks 
less than or equal to 32, which is the same constraint imposed by NumPy.

Each of the 
dimensions may optionally be identified by a unique string label, such as "x", "y", or "z". Unlabeled 
dimensions are indicated by an empty string as the label."""

from typing import List, Literal, Optional, Union

from easy_tensorstore.json_base import JsonBase


class IndexDomain(JsonBase):
    """Index domains may be serialized to/from JSON using the following schema.
    https://google.github.io/tensorstore/index_space.html#json-IndexDomain"""
    def __init__(self, 
                 rank: Optional[int] = None,
                 inclusive_min: Optional[List[Union[int, List[int]]]] = None,
                 exclusive_max: Optional[List[Union[int, List[int]]]] = None,
                 inclusive_max: Optional[List[Union[int, List[int]]]] = None,
                 shape: Optional[List[Union[int, List[int]]]] = None,
                 labels: Optional[List[str]] = None) -> None:
        
        super().__init__()
        assert 0 <= rank <= 32
        self.rank = rank
        self.inclusive_min = inclusive_min
        self.exclusive_max = exclusive_max
        self.inclusive_max = inclusive_max
        self.shape = shape
        self.labels = labels


class OutputIndexMap(JsonBase):
    """Specifies a transform from an input space to a single output index.
    Logically, an output index map is a function that maps n-dimensional input 
    index vectors to a single output index, using one of the supported output 
    index methods. This is used to represent the IndexTransform.output mapping 
    for each output dimension of an IndexTransform.
    Args:
        https://google.github.io/tensorstore/index_space.html#json-OutputIndexMap"""
    def __init__(self,
                 offset: Optional[int] = None,
                 stride: Optional[int] = None,
                 input_dimension: Optional[int] = None,
                 index_array: Optional[Union[List, int]] = None,
                 index_array_bounds: List[Union[int, Literal["-inf", "+inf"]]] = ["-inf", "+inf"]) -> None:
        super().__init__()
        self.offset = offset
        self.stride = stride
        assert input_dimension >= 0
        self.input_dimension = input_dimension
        self.index_array = index_array
        self.index_array_bounds = index_array_bounds


class IndexTransform(JsonBase):
    """An index transform from rank m to rank n maps every m-dimensional 
    index vector in a rank-m index domain to an n-dimensional index vector 
    in the output space.
    https://google.github.io/tensorstore/index_space.html#index-transform
    Args:
        https://google.github.io/tensorstore/index_space.html#json-IndexTransform"""
    def __init__(self,
                 input_rank: Optional[int] = None,
                 input_inclusive_min: Optional[List[Union[int, List[int]]]] = None,
                 input_exclusive_max: Optional[List[Union[int, List[int]]]] = None,
                 input_inclusive_max: Optional[List[Union[int, List[int]]]] = None,
                 input_shape: Optional[List[Union[int, List[int]]]] = None,
                 input_labels: Optional[List[str]] = None, 
                 output: Optional[OutputIndexMap] = None) -> None:
        super().__init__()
        assert 0<= input_rank <= 32
        self.input_rank = input_rank
        self.input_inclusive_min = input_inclusive_min
        self.input_exclusive_max = input_exclusive_max
        self.input_inclusive_max = input_inclusive_max
        self.input_shape = input_shape
        self.input_labels = input_labels
        self.output = output