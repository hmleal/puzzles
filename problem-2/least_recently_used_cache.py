import collections
import functools


class LeastRecentlyUsedCache(object):
    """
    Create LRU cache mechanism

    Args:
      max_size (int): Max size of cache
    """
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.table = collections.OrderedDict()

    def __len__(self):
        return len(self.table)

    def __setitem__(self, key, value):
        try:
            self.table.pop(key)
        except KeyError:
            if len(self) >= self.max_size:
                self.table.popitem(last=False)

        self.table[key] = value

    def __getitem__(self, key):
        try:
            value = self.table.pop(key)
            self.table[key] = value
            return value
        except KeyError:
            raise KeyError

    def __delitem__(self, key):
        try:
            del self.table[key]
        except KeyError:
            raise KeyError

    def keys(self):
        return self.table.keys()


class lrudecorator(object):
    """
    A simple decorator to use LRU in functions and speed up future calls.

    Args:
      max_size (int): Max size of cache

    Example:
      Simple way to use::
        from least_recently_used_cache import lrudecorator

        @lrudecorator(max_size=100)
        def plus(a, b):
            return a + b
    """
    def __init__(self, max_size=100):
        self.lru_cache = LeastRecentlyUsedCache(max_size)

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            key = self._generate_key(*args, **kwargs)

            try:
                return self.lru_cache[key]
            except KeyError:
                value = f(*args, **kwargs)

                self.lru_cache[key] = value

                return value

        wrapped_f.table = self.lru_cache.table

        return functools.update_wrapper(wrapped_f, f)

    def _generate_key(self, *args, **kwargs):
        kwtuple = tuple([(key, value) for key, value in kwargs.items()])

        return (args, kwtuple)
