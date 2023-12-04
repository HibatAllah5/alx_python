#Function that returns a tuple with the length of a string and its first character.
def multiple_returns(sentence):
    size = len(sentence)
    if not size:
        return ( size, None)
    else:
        return ( size, sentence[0])
    