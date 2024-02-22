"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Wyatt Fulton
Lab Time: 2:00 PM

"""


def reverse_binary():
    user_num = int(input())
    if user_num % 2 == 0:
        out_num = 0
    else:
        out_num = 1
    user_num = user_num //2
    while user_num != 0:
        new_bit = user_num % 2
        out_num = str(out_num)+str(new_bit)
        user_num = user_num // 2
    print(out_num)




if __name__ == "__main__":
    reverse_binary()