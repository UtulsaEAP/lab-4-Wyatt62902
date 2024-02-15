"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name:
Lab Time:
"""

def password_mod():
    word = input()
    password = ''
    for letter in word:
        if letter == "i":
            password = password+"1"
        if letter == "a":
            password = password+"@"
        if letter == "m":
            password = password+"M"
        if letter == "B":
            password = password+"8"
        if letter == "s":
            password = password+"$"
        else:
            password = password+str(letter)
    password = password+"!"
    print(password)

if __name__ == "__main__":
    password_mod()