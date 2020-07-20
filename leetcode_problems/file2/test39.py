# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 +5 + 1
if __name__=='__main__':
    l = [1,2,5]
    target = 11
    m = max(l)
    z = []
    for x in l:
        z.append(target//x)
    print(z)


