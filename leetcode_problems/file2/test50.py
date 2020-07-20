#1 22 11 2 1 22 """ 1 22 11 2 11 22 ......
#Input: 6
#Output: 3
#Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
if __name__=='__main__':
    a = 1
    s ='1221121221221121122'
    one = ''
    for x in range(0,len(str(a))):
        one+=s[x]
    print(one.count('1'))
