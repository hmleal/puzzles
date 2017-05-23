import unittest

from anagrams import check_anagrams


class TestAnagrams(unittest.TestCase):
    def test_car_anagrams(self):
        word = 'car'
        anagrams = ['acr', 'rca']

        self.assertListEqual(check_anagrams(word, anagrams), anagrams)

    def test_should_not_found_anagrams(self):
        word = 'brasil'
        anagrams = ['Argentina', 'Europe', 'Portugual']

        self.assertListEqual(check_anagrams(word, anagrams), [])

    def test_is_case_insensitive(self):
        word = 'DoG'
        anagrams = ['dgo', 'odg', 'ogd', 'gdo', 'god']

        self.assertListEqual(check_anagrams(word, anagrams), anagrams)

    def test_with_empty_list_of_anagrams(self):
        self.assertListEqual(check_anagrams('Rio', []), [])
