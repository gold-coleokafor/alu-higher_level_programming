#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {"I": 1, "V": 5, "X": 10, "L": 50,
              "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_string)):
        current = values.get(roman_string[i], 0)
        if i + 1 < len(roman_string):
            following = values.get(roman_string[i + 1], 0)
        else:
            following = 0
        if current < following:
            total -= current
        else:
            total += current
    return total
