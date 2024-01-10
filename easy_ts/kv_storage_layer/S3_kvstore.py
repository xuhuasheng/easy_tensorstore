"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-09 16:20:29
LastEditTime : 2024-01-10 10:28:20
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

from typing import Literal, Optional, Union

from easy_ts.constant import KVSTORE_DRIVER
from easy_ts.context_fx import Context, ContextResource

from .kvstore import KvStore


class AwsCredentials(ContextResource):
    def __init__(self,
                 profile: Optional[str] = None,
                 filename: Optional[str] = None,
                 metadata_endpoint: Optional[str] = None) -> None:
        super().__init__()
        self.profile = profile
        self.filename = filename
        self.metadata_endpoint = metadata_endpoint

class S3RequestConcurrency(ContextResource):
    def __init__(self, 
                 limit: Optional[Union[int, Literal["shared"]]] = "shared") -> None:
        super().__init__()
        self.limit = limit

class S3RequestRetries(ContextResource):
    def __init__(self,
                 max_retries: int = 32,
                 initial_delay: str = "1s",
                 max_delay: str = "32s") -> None:
        super().__init__()
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.max_delay = max_delay

class ExperimentalS3RateLimiter(ContextResource):
    def __init__(self,
                 read_rate: Optional[int] = None,
                 write_rate: Optional[int] = None,
                 doubling_time: str = "0") -> None:
        super().__init__()
        self.read_rate = read_rate
        self.write_rate = write_rate
        self.doubling_time = doubling_time


class S3_kvstore(KvStore):
    """https://google.github.io/tensorstore/kvstore/s3/index.html#s3-key-value-store-driver
    Args:
        https://google.github.io/tensorstore/kvstore/s3/index.html#json-kvstore/s3
    """
    def __init__(self, 
                 bucket: str,
                 *,
                 path: Optional[str] = None,
                 context: Optional[Context] = None,
                 requester_pays: bool = False,
                 aws_region: Optional[str] = None,
                 endpoint: Optional[str] = None,
                 host_header: Optional[str] = None,
                 aws_credentials: Optional[AwsCredentials] = None,
                 s3_request_concurrency: Optional[S3RequestConcurrency] = None ,
                 s3_request_retries: Optional[S3RequestRetries] = None,
                 experimental_s3_rate_limiter: Optional[ExperimentalS3RateLimiter] = None,
                 data_copy_concurrency: ContextResource= "data_copy_concurrency",) -> None:
        super().__init__(KVSTORE_DRIVER.s3)
        self.bucket = bucket
        self.path = path
        self.context = context
        self.requester_pays = requester_pays
        self.aws_region = aws_region
        self.endpoint = endpoint
        self.host_header = host_header
        self.aws_credentials = aws_credentials
        self.s3_request_concurrency = s3_request_concurrency
        self.s3_request_retries = s3_request_retries
        self.experimental_s3_rate_limiter = experimental_s3_rate_limiter
        self.data_copy_concurrency = data_copy_concurrency