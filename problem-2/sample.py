#!/usr/bin/env python
from least_recently_used_cache import lrudecorator


@lrudecorator(max_size=3)
def plus(a, b):
    return a + b


if __name__ == '__main__':
    print('Result: {0}'.format(plus(2, 2)))
    print('Result: {0}'.format(plus(3, 3)))
    print('Result: {0}'.format(plus(4, 4)))

    # Re-use this call and puts on the last used position
    print('Result: {0}'.format(plus(2, 2)))

    print('Print all cache table')
    print(plus.table)
