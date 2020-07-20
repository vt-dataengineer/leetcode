# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.

# Input
# [10,3,8,9,4]
# Output
# ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Expected
# ["Gold Medal","5","Bronze Medal","Silver Medal","4"]



if __name__ == '__main__':
    l = [10,3,8,9,4]
    print(l)
    s = sorted(l,reverse=True)
    print(s)
    f = []
    ll = []
    for y in range(1,len(l)+1):
        f.append(y)
    d = dict(zip(s,f))
    print(d)
    for z in l:
        if d[z] == 1:
            ll.append('Gold Medal')
        elif d[z] == 2:
            ll.append('Silver Medal')
        elif d[z] == 3:
            ll.append('Bronze Medal')
        else:
            ll.append(str(d[z]))

    print(ll)







