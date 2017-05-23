# Least recently used cache

Implement a least recently used (LRU) cache mechanism as a decorator and demonstrate it use in a small script. The LRU must be able to admit a ‘max_size’ parameter that by default has to be 100.

### Samples

1. To use in function
    ```python
    from least_recently_used_cache import lrudecorator

    @lrudecorator(max_size=100)
    def plus(a, b):
        return a + b
    ```
2. There's a simple sample file and you can run:
    ```sh
    python sample.py
    ```

### Tests

1. To run all tests:
    ```sh
    python -m unittest discover
    ```
