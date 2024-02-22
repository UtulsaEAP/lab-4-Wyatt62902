"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Wyatt Fulton
Lab Time: 2:00 PM
"""

def password_mod():
    word = input()
    password = ''
    for letter in word:
        if letter == "i":
            password = password+"1"
        elif letter == "a":
            password = password+"@"
        elif letter == "m":
            password = password+"M"
        elif letter == "B":
            password = password+"8"
        elif letter == "s":
            password = password+"$"
        else:
            password = password+str(letter)
    password = password+"!"
    print(password)

if __name__ == "__main__":
    password_mod()