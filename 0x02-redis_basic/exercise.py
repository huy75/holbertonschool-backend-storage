#!/usr/bin/env python3
""" Module for Redis db """
import redis
from uuid import uuid4
from typing import Union

class Cache:
    """ Class for methods that operate a caching system """

    def __init__(self):
        """ Instance of Redis db """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ 
        Method takes a data argument and returns a string
        Generate a random key (e.g. using uuid), store the input data in Redis
        using the random key and return the key
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
