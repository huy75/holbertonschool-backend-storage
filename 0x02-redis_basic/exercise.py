#!/usr/bin/env python3
""" Module for Redis db """
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """ Class for methods that operate a caching system """

    def __init__(self):
        """ Instance of Redis db """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self,
              data: Union[str, bytes, int, float]) -> str:
        """
        Method takes a data argument and returns a string
        Generate a random key (e.g. using uuid), store the input data in Redis
        using the random key and return the key
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieves data stored at a key
        converts the data back to the desired format
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, data: str) -> str:
        """ get a string """
        return self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """ get an int """
        return int(self._redis.get(data))
