#Function that removes all characters c and C from a string.
def no_c(my_string):
    processed = filter(lambda chr: chr not in 'cC', list(my_string))
    array = list(processed)
    response = ''.join(array)
    return response
