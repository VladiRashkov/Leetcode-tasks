# 190. Reverse Bits
# Easy
# Topics
# Companies
# Reverse bits of a given 32 bits unsigned integer.
def rev_bits(bit_num):
    rev_bit_num = ''
    for i in reversed(bit_num):
        rev_bit_num +=i
        
    number = int(rev_bit_num, 2)

    return number
a = '11111111111111111111111111111101'
print(rev_bits(a))
