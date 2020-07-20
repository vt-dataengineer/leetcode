# Input: 27
# Output: true
if __name__=='__main__':
    a = 45
    # while a != 1:
    #     a = a//3
    #     print(a)
    #
    z = a**(1/3)
    print(z)
    p = z**3
    if a==int(p):
        print('True')
    else:
        print('False')
