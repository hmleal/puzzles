import unittest

from anagrams import check_anagrams


class TestAnagrams(unittest.TestCase):
    def test_car_anagrams(self):
        word = 'car'
        anagrams = ['acr', 'rca']

        self.assertListEqual(check_anagrams(word, anagrams), anagrams)

    def test_should_not_have_anagrams(self):
        word = 'brasil'
        anagrams = ['Argentina', 'Europe', 'Portugual']

        self.assertListEqual(check_anagrams(word, anagrams), [])

    def test_is_case_insensitive(self):
        word = 'DoG'
        anagrams = ['oGd', 'gDo', 'GGG']

        self.assertListEqual(check_anagrams(word, anagrams), ['oGd', 'gDo'])
