"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Wyatt Fulton
Lab Time: Thur 2:00 PM
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    solution_found = False
    for x in range(-10, 11,1):
        for y in range(-10, 11, 1):
            if ((a*x)+(b*y)) == c and ((d*x)+(e*y) == f):
                solution_found = True
                x_sol = x
                y_sol = y
            else:
                pass


    if solution_found == True:
        print("x = "+str(x_sol)+' , y = '+str(y_sol))
    else:
        print("There is no solution")




    pass
if __name__ == "__main__":
    brute_eq()