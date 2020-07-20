# Input:  [1,2,3,4]
# Output: [24,12,8,6]
if __name__=='__main__':
    l = [1,2,3,4]
    c = []
    for i in range(1,len(l)):
        for j in range(2,len(l)):
            z = l[i]*l[j]
            t = z*l[j]
            print(t)

