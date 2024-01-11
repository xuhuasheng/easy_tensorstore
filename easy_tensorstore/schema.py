"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-08 11:23:58
LastEditTime : 2024-01-08 15:33:29
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

"""The schema of a TensorStore specifies key properties of the format in a 
uniform way that is independent of where and how the data is actually stored. 
When creating a TensorStore, schema constraints and preferences may be specified; 
the driver combines these constraints with any driver-specific constraints/defaults 
to choose a suitable schema automatically. When opening an existing TensorStore, 
its schema is validated against any constraints that are specified."""

from abc import ABCMeta
from typing import List, Literal, Optional, Union

import tensorstore as ts

from easy_tensorstore.constant import TS_DRIVER
from easy_tensorstore.index_space import IndexDomain
from easy_tensorstore.json_base import JsonBase


class ChunkLayout(JsonBase):
    """For chunked storage formats, the data storage layout can be represented 
    in a driver-independent way as a chunk layout.
    A chunk layout specifies a hierarchical regular grid with up to three levels:
    https://google.github.io/tensorstore/schema.html#json-ChunkLayout
    Args:
        - rank : integer[0, 32]¶
            Number of dimensions.
            The rank is always a hard constraint. It is redundant to specify the 
            rank if any other field that implicitly specifies the rank is included.
        - grid_origin : array of integer | null
            Specifies hard constraints on the origin of the chunk grid.
            The length must equal the rank of the index space. Each element constrains 
            the grid origin for the corresponding dimension. A value of null 
            (or, equivalently, -9223372036854775808) indicates no constraint.
        - grid_origin_soft_constraint : array of integer | null
            Specifies preferred values for the origin of the chunk grid rather than hard constraints.
            If a non-null value is specified for a given dimension in both grid_origin_soft_constraint 
            and grid_origin, the value in grid_origin takes precedence.
        - inner_order : array of integer
            Permutation specifying the element storage order within the innermost chunks.
            This must be a permutation of [0, 1, ..., rank-1]. Lexicographic order 
            (i.e. C order/row-major order) is specified as [0, 1, ..., rank-1], while colexicographic 
            order (i.e. Fortran order/column-major order) is specified as [rank-1, ..., 1, 0].
        - inner_order_soft_constraint : array of integer
            Specifies a preferred value for inner_order rather than a hard constraint. 
            If inner_order is also specified, it takes precedence.
        - write_chunk : ChunkLayout/Grid
            Constraints on the chunk grid over which writes may be efficiently partitioned.
        - read_chunk : ChunkLayout/Grid
            Constraints on the chunk grid over which reads may be efficiently partitioned.
        - codec_chunk : ChunkLayout/Grid
            Constraints on the chunk grid used by the codec, if applicable.
        - chunk : ChunkLayout/Grid
            Combined constraints on write/read/codec chunks."""
    def __init__(self,
                 rank: Optional[int] = None,
                 grid_origin: Optional[List[Optional[int]]] = None,
                 grid_origin_soft_constraint: Optional[List[Optional[int]]] = None,
                 inner_order: Optional[List[int]] = None,
                 inner_order_soft_constraint: Optional[List[int]] = None,
                 write_chunk: Optional['ChunkLayout'] = None,
                 read_chunk: Optional['ChunkLayout'] = None,
                 codec_chunk: Optional['ChunkLayout'] = None, 
                 chunk: Optional['ChunkLayout'] = None, 
                 ) -> None:
        super().__init__()
        self.rank = rank
        self.grid_origin = grid_origin
        self.grid_origin_soft_constraint = grid_origin_soft_constraint
        self.inner_order = inner_order
        self.inner_order_soft_constraint = inner_order_soft_constraint
        self.write_chunk = write_chunk
        self.read_chunk = read_chunk
        self.codec_chunk = codec_chunk
        self.chunk = chunk


class ChunkLayoutGrid(JsonBase):
    """Constraints on the write/read/codec chunk grids.
        When creating a new TensorStore, the chunk shape can be specified directly 
        using the shape and shape_soft_constraint members, or indirectly by specifying 
        the aspect_ratio and target number of elements.
        When opening an existing TensorStore, the preferences indicated by 
        shape_soft_constraint, aspect_ratio, aspect_ratio_soft_constraint, elements, 
        and elements_soft_constraint are ignored; only shape serves as a constraint.
        Args:
           https://google.github.io/tensorstore/schema.html#json-ChunkLayout/Grid"""
    def __init__(self, 
                 shape: Optional[Union[List[int], int, Literal['null']]] = None,
                 shape_soft_constraint: Optional[Union[List[int], int, Literal['null']]] = None,
                 aspect_ratio: Optional[Union[List[int], Literal['null']]] = None,
                 aspect_ratio_soft_constraint:  Optional[Union[List[int], Literal['null']]] = None,
                 elements: Optional[Union[int, Literal['null']]] = None,
                 elements_soft_constraint: Optional[Union[int, Literal['null']]] = None) -> None:
        super().__init__()
        self.shape = shape
        self.shape_soft_constraint = shape_soft_constraint
        self.aspect_ratio = aspect_ratio
        self.aspect_ratio_soft_constraint = aspect_ratio_soft_constraint
        self.elements = elements
        self.elements_soft_constraint = elements_soft_constraint


class Codec(JsonBase, metaclass=ABCMeta):
    """Codecs are specified by a required driver property that identifies the driver. 
    All other properties are driver-specific. Refer to the driver documentation for 
    the supported codec drivers and the driver-specific properties.
    https://google.github.io/tensorstore/schema.html#json-Codec
    Args:
        - driver : string
            Driver identifier
            Specifies the TensorStore driver to which this codec is applicable.
    Examples:
        >>> {
        >>>     "driver": "zarr",
        >>>     "compressor": {"id": "blosc", "cname": "lz4", "clevel": null, "5": null, "shuffle": 1},
        >>>     "filters": null
        >>> }
        >>> {
        >>>     "driver": "n5",
        >>>     "compression": {"type": "gzip", "level": "6", "useZlib": false}
        >>> }
    """
    def __init__(self, driver: TS_DRIVER) -> None:
        super().__init__()
        self.driver = driver.value


class Schema(JsonBase):
    """
    Args:
        - rank : integer[0, 32]
            Number of dimensions.
            The rank is always a hard constraint. 
        - dtype : dtype
            Specifies the data type of the TensorStore.
            The data type is always a hard constraint.
        - domain : IndexDomain
            Domain of the TensorStore, including bounds and optional dimension labels.
            The domain is always a hard constraint, except that a labeled dimension is 
            allowed to match an unlabeled dimension, and an implicit, infinite bound is 
            considered an unspecified bound and does not impose any constraints. When 
            merging two schema constraint objects that both specify domains, any dimensions 
            that are labeled in both domains must have the same label, and any explicit 
            or finite bounds specified in both domains must be equal. If a dimension is 
            labeled in one domain and unlabeled in the other, the label is retained. If 
            a bound is implicit and infinite in one domain, the bound from the other 
            domain is used.
        - chunk_layout : ChunkLayout
            Data storage layout constraints.
            The rank of the chunk layout must match the rank of the schema. When merging 
            schema constraints objects, the chunk layout constraints are merged recursively.
        - codec : Codec
            Driver-specific compression and other parameters for encoding/decoding data. 
            When merging schema constraints objects, the codec constraints are merged recursively.
        - fill_value
            Fill value to use for missing data.
            Must be broadcast-compatible with the domain.
        - dimension_units : array of Unit | null
            Physical units of each dimension.
            Specifies the physical quantity corresponding to an increment of 1 index along 
            each dimension, i.e. the resolution. The length must match the rank of the schema. 
            Specifying null for a dimension indicates that the unit is unknown.
            >>> ["4nm", "4nm", null] 
            specifies that the voxel size is 4nm along the first two dimensions, and unknown along the third dimension."""

    def __init__(self,
                 rank: Optional[int] = None,
                 dtype: Optional[ts.dtype] = None,
                 domain: Optional[IndexDomain] = None,
                 chunk_layout : Optional[ChunkLayout] = None,
                 codec: Optional[Codec] = None,
                 fill_value: Optional[Union[int, float]] = None,
                 dimension_units: Optional[List[Optional[str]]] = None
                 ) -> None:
        super().__init__()
        assert 0 <= rank <= 32
        self.rank = rank
        self.dtype = dtype
        self.domain = domain
        self.chunk_layout = chunk_layout
        self.codec = codec
        self.fill_value = fill_value
        self.dimension_units = dimension_units






