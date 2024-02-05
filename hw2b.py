import math

def fcn1(x):
    """Defines Function#1"""
    return x - 3 * math.cos(x)
def fcn2(x):
    """Defines Function#2"""
    return math.cos(2*x) * x**3
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """Uses the secant method to find the root of the called function fcn 1 or 2. Returns: root of the function"""
    # set starting values for variables
    n = 0
    xm = 0
    xi = 0
    if math.fabs(fcn(x0) - fcn(x1)) > xtol: # checking for valid initial guesses
        while True:

            # calculate the intermediate value
            xi = ((x0 * fcn(x1) - x1 * fcn(x0)) / (fcn(x1) - fcn(x0)))

            # update the value of interval
            x0 = x1
            x1 = xi

            # update number of iteration
            n += 1
            xm = ((x0 * fcn(x1) - x1 * fcn(x0)) / (fcn(x1) - fcn(x0)))


            if (abs(xm - xi) < xtol): # check xm against xtol
                print(f"Reached needed accuracy")
                break

            if n >= maxiter: # check n against max iterations
                print("Reached maximum number of iterations")
                break
        # print results
        print("Root of the given equation =",
              round(xi, 8))
        print("No. of iterations = ", n)


    else:
        print("Check initial guesses")




def main():
    """prints the equation function used, then calls and prints results of the Secant function"""
    print("fcn1") #identifying function used
    Secant(fcn1,1, 2, 5, 1 * 10**-4)
    print() # adds empty line to increase legibility
    print("fcn2")
    Secant(fcn2, 1, 2, 15, 1 * 10 ** -8)
    print()
    print("fcn2")
    Secant(fcn2, 1, 2, 3, 1 * 10 ** -8)

main()
