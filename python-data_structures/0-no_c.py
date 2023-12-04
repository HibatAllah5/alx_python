#Function that removes all characters c and C from a string.
def no_c(my_string):
    my_new_string = no_c('')
    for letters in my_string:
        if letters != "c" and letters != "C":
            my_new_string += letters
    return my_new_string        
