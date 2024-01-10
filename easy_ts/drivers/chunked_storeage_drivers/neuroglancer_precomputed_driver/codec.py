from typing import Optional, Literal

from easy_ts.constant import TS_DRIVER
from easy_ts.schema import Codec


class NPCodec(Codec):
    def __init__(self, 
                 encoding : Optional[Literal["raw", "jpeg", "compressed_segmentation"]] = None,
                 jpeg_quality: int = 75,
                 shard_data_encoding: Optional[Literal["raw", "gzip"]] = None) -> None:
        super().__init__(driver=TS_DRIVER.neuroglancer_precomputed)
        self.encoding = encoding
        self.jpeg_quality = jpeg_quality
        self.shard_data_encoding = shard_data_encoding
