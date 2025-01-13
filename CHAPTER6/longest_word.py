def longest_word(words):
    """
    words is a list of words

    Return the longest word from the list wth the most characters.
    If there are multiple words with the same length, return the first one.
    >>> longest_word(['apple', 'banana', 'pear', 'grapefruit'])
    'grapefruit'
    """
    longest = ''
    for i in range(0, len(words)):
        if len(words[i]) > len(longest):
            longest = words[i]
    return longest
import doctest
doctest.testmod(verbose=True)