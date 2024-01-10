"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2024-01-05 15:42:25
LastEditTime : 2024-01-08 11:23:44
LastEditors  : aircas41-server-win xuhs@aircas.ac.cn
Copyright (c) 2024 AIRCAS. All rights reserved. 
"""

"""Configuration options for TensorStore drivers are specified using a context 
framework, which allows resources such as cache pools, concurrent execution pools, 
and authentication credentials to be specified using JSON in a way that allows 
sharing of resources by multiple TensorStore drivers."""


from abc import ABCMeta
from typing import Literal, Union

from .json_base import JsonBase


class Context(JsonBase):
    """A context JSON object is a mapping of resource identifiers 
    to ContextResource specifications.
    Args:
        - <resource-type> : ContextResource.
            Overrides the default resource for the given <resource-type>, 
            which must be a supported resource type.
        - <resource-type>#<id> : ContextResource.
            Defines a resource with identifier <id> of the given <resource-type>. 
            The resource specification must be compatible with <resource-type>.
    Example:
        >>> {
        >>>     "cache_pool": {"total_bytes_limit": 10000000},
        >>>     "cache_pool#remote": {"total_bytes_limit": 100000000},
        >>>     "data_copy_concurrency": {"limit": 8}
        >>> }
    """
    def __init__(self, **kwargs) -> None:
        super().__init__()
        for k, v in kwargs.items():
            assert (k.startswith('cache_pool') or k.startswith('cache_pool#') or 
                    k.startswith('data_copy_concurrency') or k.startswith('data_copy_concurrency#'))
            assert isinstance(v, ContextResource)
            setattr(self, k, v)


class ContextResource(JsonBase, metaclass=ABCMeta):
    """Specifies a context resource of a particular <resource-type>.
    Args:
        - object | boolean | number: Specifies the resource directly. 
            Any constraints on the value are determined by the particular <resource-type>.
        - string: References another resource of the same type in the 
            current or parent context using the syntax "<resource-type>" or 
            "<resource-type>#<id>", where <resource-type> matches the type 
            of this resource.
        - null: Specifies a new instance of the default resource of the 
            given <resource-type>. Only valid within a Context specification."""
    def __init__(self) -> None:
        super().__init__()


class CachePool(ContextResource):
    """Specifies the size of an in-memory Least Recently Used (LRU) cache. 
    Each cache_pool resource specifies a separate memory pool.
    Args:
        - total_bytes_limit : integer[0, +∞) = 0
            Soft limit on the total number of bytes in the cache. The 
            least-recently used data that is not in use is evicted from 
            the cache when this limit is reached.
        - queued_for_writeback_bytes_limit : integer[0, +∞)
            Soft limit on the total number of bytes of data pending writeback. 
            Writeback is initated on the least-recently used data that is pending 
            writeback when this limit is reached. Defaults to half of total_bytes_limit."""
    def __init__(self, 
                 total_bytes_limit: int = 0, 
                 queued_for_writeback_bytes_limit: int = 0) -> None:
        super().__init__()
        assert total_bytes_limit >= 0
        assert queued_for_writeback_bytes_limit >= 0
        self.total_bytes_limit = total_bytes_limit
        self.queued_for_writeback_bytes_limit = queued_for_writeback_bytes_limit


class DataCopyConcurrency(ContextResource):
    """Specifies a limit on the number of CPU cores used 
    concurrently for data copying/encoding/decoding.
    Args:
        - limit : integer[1, +∞) | "shared" = "shared"
            The maximum number of CPU cores that may be used. If 
            the special value of "shared" is specified, a shared 
            global limit equal to the number of CPU cores/threads 
            available applies."""
    def __init__(self, limit: Union[int, Literal['shared']] = 'shared') -> None:
        super().__init__()
        if isinstance(limit, int):
            assert limit >=1
        elif isinstance(limit, str):
            assert limit == 'shared'
        else:
            raise ValueError("limit is not expected")
        self.limit = limit











