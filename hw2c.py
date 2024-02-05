
def diag(Aaug):
    """Checking for diagonal dominance Returns: result of check and info if false"""
    m=Aaug # aliasing for shortened code
    limit = len(Aaug[0]) - 1 # getting size of matric with 0 index offset

    for i in range(0, limit): # looping through the rows
        sum = 0 # reset sum to 0
        for j in range(0, limit): # looping through columns
            sum = sum + abs(m[i][j]) # summing entire row

        sum = sum - abs(m[i][i]) # removing diag from sum

        if (abs(m[i][i]) < sum): # checking if sum is greater than diag number
            l = abs(m[i][i])
            return [False, i+1, abs(m[i][i]), sum] # returning info to give to user


def GaussSeidel(Aaug,Niter=15):
    """Performs the Gauss Seidel method of estimation and returns the estimated values"""

    its = 0 # resetting iterations to 0
    limit = len(Aaug[0])-1 # getting matrix size with index offset
    x = [0 for i in range(limit)]

    for count in range(limit):
        x[count] = 0

    # Gauss-Jordan elimination
    while True:
        its += 1
        for count in range(limit): # looping through rows
            temp = Aaug[count][limit] # defining temp variable
            for t in range(limit): # looping through columns
                if t != count:
                    temp -= Aaug[count][t] * x[t]
            temp /= Aaug[count][count]
            x[count] = temp
        if its >= Niter: # breaks when iteration limit is reached
            break

    for count in range(limit): # printing solution
        print(f" x[{count + 1}]:  ", "{:.3f}".format(x[count]))

def main():
    """calls gaussSeidel function and prints results"""
    print("Solution to Matrix 1")
    Aaug = [[3, 1, -1, 2], [1, 4, 1, 12], [2, 1, 2, 10]] #defining the matrix
    result1 = diag(Aaug)
    if result1 is not None: # condition for if diag dom comes back false
        print(f"    Not DiagDom! Row: {result1[1]}, Sum of nonDiags({result1[3]}) > Diag({result1[2]})")
        print("Running GaussSeidel Function anyway")
    GaussSeidel(Aaug) #calling gausseidel function

    print()
    print("Solution to Matrix 2")
    Aaug = [[1,-10, 2, 4, 2], [3, 1, 4, 12, 12], [9, 2, 3, 4, 21], [-1, 2, 7, 3, 37]] #defining the matrix
    result1 = diag(Aaug)
    if result1 is not None:
        print(f"    Not DiagDom! Row: {result1[1]}, Sum of nonDiags({result1[3]}) > Diag({result1[2]})")
        print("Running GaussSeidel Function anyway")
    GaussSeidel(Aaug)

    # Testing matrix, is diagdom
    # print()
    # print("Solution to Matrix 2")
    # Aaug = [[3, -2, 1, 4], [1, 3, 2, 12], [-1, 2, 4, 4]]
    # result1 = diag(Aaug)
    # if result1 is not None:
    #     print(f" Not DiagDom! Row: {diag(Aaug)[1]}, Sum of nonDiags({diag(Aaug)[3]}) > Diag({diag(Aaug)[2]})")
    #     print("Running GaussSeidel Function anyway")
    # GaussSeidel(Aaug)

main()
