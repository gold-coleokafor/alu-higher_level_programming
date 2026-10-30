#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best = None
    for k in a_dictionary:
        if best is None or a_dictionary[k] > best:
            best = a_dictionary[k]
            best_key = k
    return best_key
