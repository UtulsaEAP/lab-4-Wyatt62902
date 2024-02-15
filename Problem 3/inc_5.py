"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name:
Lab Time:
"""

def inc_5():
    user_start = int(input())
    user_end = int(input())
    series = ''
    if user_start < user_end:
        while user_start <= user_end:
            series += str(user_start) + ' '
            user_start += 5
            
        print(series + '\n')
    elif user_start == user_end:
        print(str(user_start)+ ' \n')
    else:
        print("Second integer can't be less than the first.")

if __name__ == '__main__':
    inc_5()