import doctest
def count_words(words):
    """
    >>> words = ["Dan", "danger", "Leo"]
    >>> count_words(words)
    1
    """
    count = 0
    for word in words:
        if word == "Dan":
            count += 1
    return count
doctest.testmod(verbose=True)
