def is_palindrome(sequence):
     if len(sequence) == 0:
        return True
     return is_palindrome(sequence[1:-1]) if sequence[0] == sequence[len(sequence)-1] else False

word = 'bob'
print(is_palindrome(word))

