# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
if __name__=='__main__':
    l = [1,2,3,1]
    c = 0
    d = 0
    for x in range(len(l)):
        if x%2 == 0:
            c+=l[x]
            print('c = '+str(c))
        else:
            d+=l[x]
            print('d = '+str(d))
    print('c = : '+str(c))
    print('d = : '+str(d))
    print('The largest robbery is: '+str(max(c,d))+'$')

