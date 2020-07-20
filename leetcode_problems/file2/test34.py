# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
if __name__=='__main__':
    l = [0,1]
    s = sorted(l)
    #print(sorted(l))
    if len(l)==1 and l.__contains__(0):
        print(1)
    else:
        for x in range(0,max(l)+1):
            if x not in s:
                print(x)

