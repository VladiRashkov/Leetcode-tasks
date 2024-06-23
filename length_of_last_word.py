def sentence(s):
    reverse_s = reversed(s)
    count=0
    word = ''
    tick = False
    for i in reverse_s:
        if i != ' ':
            word+=i
            count+=1
            tick = True
        else:
            if tick==True:
                break
            else:
                continue
            
    the_word = ''.join(reversed(word))
    return f'The last word is "{the_word}" with length {count}'


print(sentence(input()))