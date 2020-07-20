# Input: [2,2,1,1,1,2,2]
# Output: 2
if __name__=='__main__':
    l = [2,2,1,1,1,2,2]
    s = set(l)
    print(max(l.count(2),l.count(1)))
