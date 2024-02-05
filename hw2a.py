
import math

def PDF(x):
    """defining the normal probability density function
    Returns: Nothing, only sets the equation"""
    return ((1 / (args[1] * math.sqrt(2 * math.pi))) * math.exp((-.5) * ((((x-args[0])/args[1]))**2)))

def getGT():
    """Asking if the probability is going to be for greater than or less than
    Returns: Boolean to be used Probability function"""
    GT=str.lower(input("GT True or False:")) # asking if user wants < or >
    if GT=="true":
        return True
    if GT == "false":
        return False
def Probability(PDF, args ,c, GT=True):
    """calculating the probability by integrating the PDF function by simpsons 1/3 rule
    Returns: The Probability x is < or > c"""
    xn = c # sets upper limit of integration
    x0 = args[0] - (5 * args[1]) # set lower limit of integration
    n = 10 # setting num of segments
    h = (xn - x0) / n #step size

    integration = PDF(x0) + PDF(xn) # Finding sum

    for i in range(1, n):
        k = x0 + i * h

        if i % 2 == 0:  # separating and multiplying evens and odds
            integration = integration + 2 * PDF(k)
        else:
            integration = integration + 4 * PDF(k)

    integration = integration * h / 3     # Finding final integration value
    if GT==True: # changing prob to represent if user wanted < or >
        return 1-integration, True
    else:
        return integration, False


def main():
    """main function, runs the probability function
    Returns: Prints the results of the probability function"""
    result = Probability(PDF, args, c, GT) # calling probability function
    prob = float("{:.3f}".format(result[0])) # pulling probability out of result

    if result[1] == True: # pulling sign choice(<,>) out of result
        print(f"P(x>{c}|N({args[0]},{args[1]}))= {prob} ")
    else:
        print(f"P(x<{c}|N({args[0]},{args[1]}))= ", prob)


args = 100, 12.5 #args = Population mean, Population Standard Dev
c = 105  # Upper limit of integration
GT = False # choosing < or >
main()

args = 100, 3  #args = Population mean, Population Standard Dev
c = args[0] + 2*args[1] # Upper limit of integration
GT= True # choosing < or >
main()

# defining args, c, and GT using user inputs
args = float(input("Enter new population mean:")), float(input("Enter new population standard deviation:"))
c = float(input('Enter new upper limit of integration: '))
GT = getGT()
main()