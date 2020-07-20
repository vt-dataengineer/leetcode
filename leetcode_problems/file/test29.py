# Input: 13
# Output: 6
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
if __name__ == '__main__':
    a = str(13)
    c=0
    for i in range(1,int(a)+1):
        if '1' in str(i):
            c+=1
            print(i)
    print(c)
