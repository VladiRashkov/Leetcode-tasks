sum_nums = 0
second_num = 0
pow = 0
def check_number(num):
    if num == 0:
        return 0
    global second_num
    if second_num == 0:
        second_num = num
        global pow
        pow = len(str(second_num))
    
    current_number = num%10
    global sum_nums
    sum_nums+=current_number**pow
    check_number(num//10)

    return sum_nums == second_num
number = int(input())
if check_number(number):
    print('Yes')
else:
    print('No')