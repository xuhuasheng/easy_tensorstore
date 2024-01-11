
from typing import List, Literal, Optional, TypeVar

from easy_tensorstore.json_base import JsonBase

from .compression import N5Compression


class N5Metadata(JsonBase):
    data_type = TypeVar("data_type", Literal["uint8", "uint16", "uint32", "uint64", "int8", "int16", "int32", "int64", "float32", "float64"])
    def __init__(self,
                 dimension: Optional[List[int]] = None,
                 blockSize: Optional[List[int]] = None,
                 dataType: Optional[data_type] = None,
                 axes: Optional[List[str]] = None,
                 units: Optional[List[str]] = None,
                 resolution: Optional[List[int]] = None,
                 compression: Optional[N5Compression] = None) -> None:
        super().__init__()
        self.dimension = dimension
        self.blockSize = blockSize
        self.dataType = dataType
        self.axes = axes
        self.units = units
        self.resolution = resolution
        self.compression = compression