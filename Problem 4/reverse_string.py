"""
Complete the following python code to reverse the string entered by the user.

Name: Wyatt Fulton
Lab Time: Thur 2:00PM
"""

def reverse_string():
    print_string = ''
    reverse_string = input()
    while (reverse_string != "Done") and (reverse_string != "done") and (reverse_string != 'd'):
        reverse_list = range(len(reverse_string)-1,-1,-1)
        for i in reverse_list:
            print_string = print_string + reverse_string[i]
        print(print_string)
        print_string = ''
        reverse_string = input()

            
    
        

    
    pass
if __name__ == "__main__":
    reverse_string()

#reverse_string()