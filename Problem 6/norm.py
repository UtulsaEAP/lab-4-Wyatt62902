"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Wyatt Fulton
Lab Time: 2:00 PM
"""

def norm():
    num_remaining = int(input())
    num_array = [0] * num_remaining
    array_pointer = 0
    while num_remaining > array_pointer:
        num_array[array_pointer] = float(input())
        array_pointer += 1
    
    for j in num_array:
        for i in num_array:
            if i > j:
                greatest_num = i
            else: 
                pass

    for j in num_array:
        print(f'{(j / greatest_num):.2f}')

    pass

if __name__ == "__main__":
    norm()