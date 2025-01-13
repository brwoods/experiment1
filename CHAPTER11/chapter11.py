# Description: This program is a text analysis program that uses a signature to determine the author of a text.
# Date: 01/12/2025
# Author: Bruce Woods as found in Learn AI-Assisted Python Programming, 2nd Edition by Leo Porter and Daniel Zingaro 
import string

def clean_word(word):
    """
    word is a string. 
    
    Return a version of word in which all letter have been converted to lowercase, and punctuation character have 
    been stripped from both ends. 
    Inner punctuation is left untouched.
    >>> clean_word('Pearl!')
    'pearl'
    >>> clean_word('card-board')
    'card-board'
      
    """
    # Convert to lowercase
    word = word.lower()
    # Strip punctuation from both ends
    return word.strip(string.punctuation)
def average_word_length(text):
    """
    text is a string of text.

    Return the average word length of the words in text.
    Do not count empty words as words.
    Do not include surrounding punctuation.
    >>> average_word_length('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    4.1

    """
    words = text.split()
    total = 0
    count = 0
    for word in words:
        word = clean_word(word)
        if word != '':
            total += len(word)
            count += 1
    return total / count
def different_to_total(text):
    """
    text is a string of text.

    Return the number of unique words in text divided by the total number of words in text.
    Do not count empty words as words.
    Do not include surrounding punctuation.
    >>> different_to_total('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    0.7

    """
    words = text.split()
    total = 0
    unique = set()
    for word in words:
        word = clean_word(word)
        if word != '':
            total += 1
            unique.add(word)
    return len(unique) / total
def exactly_once_to_total(text):
    """
    text is a string of text.

    Return the number of words that appear exactly once in text divided by the total number of words in text.
    Do not count empty words as words.
    Do not include surrounding punctuation.
    >>> exactly_once_to_total('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    0.5

    """
    words = text.split()
    total = 0
    unique = set()
    once = set()
    for word in words:
        word = clean_word(word)
        if word != '':
            total += 1
            if word in unique:
                once.discard(word)
            else:
                unique.add(word)
                once.add(word)
    return len(once) / total
def split_string(text, separators):
    """
    text is a string of text.
    separators is a string of separator characters.

    Split text into a list of words, using the characters in separators as separators and return the result.
    Remove spaces from beginning and end of a string before adding it to the list.
    Do not include empty strings in the list.
    >>> split_string('one*two[three', '*[')
    ['one', 'two', 'three']
    >>> split_string('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.', '.?!')
    ['A pearl', 'Pearl', 'Lustrous pearl', 'Rare', 'What a nice find']
    """
    
    words = []
    word = ''
    for char in text:
        if char in separators:
            word = word.strip()
            if word != '':
                words.append(word)
            word = ''
        else:
            word += char
    word = word.strip()
    if word != '':
        words.append(word)
    return words
def get_sentences(text):
    """
    text is a string of text.

    Return a list of sentences from text.
    Sentences are separated by a '.', '?' or '!'.

    >>> get_sentences('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    ['A pearl', 'Pearl', 'Lustrous pearl', 'Rare', 'What a nice find']
    """
    return split_string(text, '.?!')
def average_sentence_length(text):
    """
    text is a string of text.

    Return the average number of words per sentence in text.
    Do not count empty words as words.
    >>> average_sentence_length('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    2.0

    """
    sentences = get_sentences(text)
    total = 0
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word != '':
                total += 1
    return total / len(sentences)
def get_phrases(sentence):
    """
    sentence is a sentence string.

    Return a list of phrases from sentence.
    Phrases are separated by a ',', ';' or ':'.

    >>> get_phrases('Lustrous pearl, Rare, What a nice find')
    ['Lustrous pearl', 'Rare', 'What a nice find']
    
    """
    return split_string(sentence, ',;:')
def average_sentence_complexity(text):
    """
    text is a string of text.

    Return the average number of phrases per sentence in text.
    Do not count empty words as words.
    >>> average_sentence_complexity('A pearl! Pearl! Lustrous pearl! Rare, What a nice find.')
    1.25

    """
    sentences = get_sentences(text)
    total = 0
    for sentence in sentences:
        phrases = get_phrases(sentence)
        total += len(phrases)
    return total / len(sentences)
def make_signature(text):
    """
    The signature for text is a list of five elements:
    average word length, different words divided by total words,
    words that appear exactly once divided by total words,
    average sentence length, average sentence complexity.

    Return the signature for text.

    >>> make_signature('A pearl! Pearl! Lustrous pearl! Rare, What a nice find.')
    [4.1, 0.7, 0.5, 2.5, 1.25]

    """
    return [average_word_length(text), different_to_total(text), exactly_once_to_total(text), average_sentence_length(text), average_sentence_complexity(text)]
import os
def get_all_signatures(known_dir):
    """
    known_dir is the name of a directory of books.
    For each file in directory known_dir, determine its signature.

    Return a dictionary where each key is the name of a file, and the value is its signature.
    """
    signatures = {}
    for filename in os.listdir(known_dir):
        with open(os.path.join(known_dir, filename), encoding='utf-8', errors='ignore') as f:
            text = f.read()
            signatures[filename] = make_signature(text)
    return signatures
def get_score(signature1, signature2, weights):
    """
    signature1 and signature2 are signatures.
    weights is a list of five wights.

    Return the score of signature1 and signature2.
    >>> get_score([4.6, 0.1, 0.05, 10, 2], [4.3, 0.1, 0.04, 16, 4], [11, 33, 50, 0.4, 4])
    14.2
    """
    score = 0
    for i in range(5):
        score += abs(signature1[i] - signature2[i]) * weights[i]
    return score
def lowest_score(signatures_dict, unknown_signature, weights):
    """
    signatures_dict is a dictionary mapping keys to signatures.
    unknown_signature is a signature.
    weights is a list of five weights.
    Return the key whose signature value has the lowest score with unknown_signature.

    >>> d ={'Dan': [1,1,1,1,1], 'Leo': [3,3,3,3,3]}
    >>> unknown = [1, 0.8, 0.9, 1.3, 1.4]
    >>> weights = [11, 33, 50, 0.4, 4]
    >>> lowest_score(d, unknown, weights)
    'Dan'
    """
    lowest = None
    for key in signatures_dict:
        score = get_score(signatures_dict[key], unknown_signature, weights)
        if lowest is None or score < lowest[1]:
            lowest = (key, score)
    return lowest[0]
def process_data(mystery_filename, known_dir):
    """
    mystery_filename is the filename of a mystery book whose author we want to know.
    known_dir is the name of a directory of books.

    Return the name of the signature closest to the signature of the text of mystery_filename.
    """
    signatures = get_all_signatures(known_dir)  
    with open(mystery_filename, encoding='utf-8', errors='ignore') as f:
        text = f.read() 
        unknown_signature = make_signature(text)
    return lowest_score(signatures, unknown_signature, [11, 33, 50, 0.4, 4])
def make_guess(known_dir):
    """
    Asks user for a filename.
    Get all known signatures from known_dir, and print the name of the one that has the lowest score with the user's filename.
    """
    filename = input("Enter the filename of the mystery text: ")
    result = process_data(filename, known_dir)
    print(f"The author with the closest signature is: {result}")
make_guess('known_authors')
#import doctest
#doctest.testmod(verbose=True)