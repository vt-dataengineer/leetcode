# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
if __name__=='__main__':
    l = [0,1,0,3,12]
    s= []
    t = []
    for x in l:
        if x != 0:
            s.append(x)
        else:
            t.append(x)
    print(s+t)
    print(l)
