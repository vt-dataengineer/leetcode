# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
if __name__=='__main__':
    l = [1,1,2,3,3,4,4,8,8]
    for x in l:
        if l.count(x)==1:
            print(x)
