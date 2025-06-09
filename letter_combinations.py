def letter_combinations(dialed_num):
    
    num_letter_pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                      '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
                      }
    
    if dialed_num == ' ':
        return []
   
        
    l_num = list(dialed_num)
    iter = 0
    collection = []
    curr_var = ''
    if len(dialed_num) == 1:
        current = l_num[iter]
        variations = num_letter_pad[current]
        for var in variations:
            collection.append(var)
        return collection
    while True:
        current = l_num[iter]  # 2
        variations = num_letter_pad[current]
        for var in variations:
            next = l_num[iter+1]
            next_variations = num_letter_pad[next]
            for next in next_variations:
                curr_var += var
                curr_var += next
                collection.append(curr_var)
                curr_var = ''
        break
    return collection


dial = input()
print(letter_combinations(dial))

# ["ad","ae","af","bd","be","bf","cd","ce","cf"]
