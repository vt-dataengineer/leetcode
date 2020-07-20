# Input: 13
# Output: 6
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
if __name__=='__main__':
    a = 21
    b = str(a)
    for i in range(1,a+1):
       # print(i)
        n = str(i)
        if n.__contains__('1'):
            print(n)
