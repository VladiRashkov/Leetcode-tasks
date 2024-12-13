def roman_to_int(roman_num):

    roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}

    arabic_num = 0
    prev_value = 0

    for char in reversed(roman_num):
        current_value = roman_to_arabic[char]

        if current_value < prev_value:
            arabic_num -= current_value
        else:
            arabic_num += current_value
        prev_value = current_value

    return arabic_num



print(roman_to_int('MCMXCIV'))  


# I, II, III, IV, V, VI, VII, VIII, IX, X
# XL 40, L 50, LC 90, C 100
# CD 400, D 500, CM 900, M 1000
