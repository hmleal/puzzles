def check_anagrams(word, anagrams):
    """Find anagrams.

    Check valid anagrams for the word inside the given words.

    Args:
      word (str): word to check valid anagrans in the given words.
      anagrams (list): List of word to check if is a anagram.

    Returns:
      list: List with all valid anagrans to a given word
    """
    sorted_word = sorted(word.lower())

    return [a for a in anagrams if sorted(a.lower()) == sorted_word]
