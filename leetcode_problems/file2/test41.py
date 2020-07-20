# Input: a = 2, b = [1,0]
# Output: 1024
# mod 1337
if __name__=='__main__':
    a = 2
    b = [1,0]
    s = ''
    for x in b:
        s = s+str(x)
    i = int(s)
    res = (a.__pow__(i))%1337
    print(res)


