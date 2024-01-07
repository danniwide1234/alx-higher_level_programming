#!/usr/bin/python3
def multiple_returns(sentence):
    required_tuple = ()
    if len(sentence) == 0:
        required_tuple = 0, "None"
    else:
        required_tuple = len(sentence), sentence[0]
    return required_tuple
