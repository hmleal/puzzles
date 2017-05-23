import unittest

from least_recently_used_cache import LeastRecentlyUsedCache

class TestLastRecentCache(unittest.TestCase):
    def setUp(self):
        self.lru = LeastRecentlyUsedCache(max_size=3)

        self.lru['key1'] = 'value1'
        self.lru['key2'] = 'value2'
        self.lru['key3'] = 'value3'

    def test_should_respect_max_size(self):
        self.lru['key4'] = 'value4'

        self.assertEqual(len(self.lru), 3)

    def test_more_older_is_lost_when_max_size_is_exceded(self):
        self.lru['key4'] = 'value4'

        with self.assertRaises(KeyError):
            self.lru['key1']

    def test_last_used_most_be_in_first(self):
        self.assertListEqual(self.lru.keys(), ['key1', 'key2', 'key3'])

    def test_least_used_most_be_in_last(self):
        self.lru['key1']

        self.assertListEqual(self.lru.keys(), ['key2', 'key3', 'key1'])
