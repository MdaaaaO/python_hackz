
import re

WordMap = {
    "team": 1,
    "dinner": 2,
    "breakfast": 4,
    "planned": 8,
    "Walnut Creek": 16,
    "Concord": 32,
    "afternoon": 64,
    "morning": 128,
    "evening": 256,
    "tonight": 512
}

def sanitize(sentence: str) -> list:
    """Given an input string (sentence) will remove all special characters, duplicated words and returns a list of words.
    """

    # log input
    print("sanitize: incoming sentence is: %s" % sentence)

    # sanitize
    sentence = re.sub('[^A-Za-z0-9 ]+', '', sentence)

    # split the incoming sentence by white space, reteurn list
    split_word = sentence.split(" ")

    # use only unique words for bitflags
    unique_words = set(split_word)

    # log output
    print("sanitize: returning: %s" % unique_words)

    # return
    return unique_words

def encode(words: list) -> str:
    """Given a string, will encode most essential words to generate bitflag code.
    """

    # access the global dictionary for words
    global WordMap

    # helper variables
    _code = 0
    _matched = []

    # iterate thorough all unique words
    for word in words:

        # check if that words has a flag assigned
        if word in list(WordMap.keys()):

            # append to the matched list
            _matched.append(word)

            # increment the code based on the assigned code
            _code += WordMap[word]

    # log
    print("encode: matched on words %s, calculated flag: %s" % (_matched, _code))

    # return the code
    return _code

def decode(code: int) -> str:
    """Given a int, will decode to get the most essential words.
    """

    # access the global dictionary for word
    global WordMap

    # invert WordMap for fast access / hashmap like
    invertWordMap = {value: key for key, value in WordMap.items()}

    # get all flags (keys) from the dictionary and sort them in reversed order (highest first)
    reverse_sorted_flags = sorted(list(invertWordMap.keys()), reverse=True)

    # holds words matched
    _words = []

    # iterate flags, start with the highest one
    for flag in reverse_sorted_flags:

        # on flag is bigger than code
        if flag > code:

            # no match continue with the next smaller flag
            continue

        # if flag is within the code
        elif flag <= code:

            # append the matched word for that flag
            _words.append(invertWordMap[flag])

            # remove the value of the flag from the code
            code -= flag

    print("decode: matched on words %s" % _words)

    return _words

def main():
    """This is the main entry point of this python file.
    """

    # input, can be by user
    sentence = "Hey Team! Let's have some team dinner planned for next Wednesday in Concord."

    # remove special charecters from input
    unique_words = sanitize(sentence=sentence)

    # encode the input
    encoded = encode(words=unique_words)

    # decode the code
    decoded = decode(code=encoded)

# execute
main()
