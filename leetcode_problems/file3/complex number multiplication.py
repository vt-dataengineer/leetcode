# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
if __name__=='__main__':
    a = '1+1i'
    b = '1+1i'


    A = [int(x) for x in a.replace('i','').split('+')]
    B = [int(x) for x in b.replace('i','').split('+')]
    print(str(A[0]*B[0]-A[1]*B[1])+'+'+str(A[0]*B[1]+A[1]*B[0])+'i')
