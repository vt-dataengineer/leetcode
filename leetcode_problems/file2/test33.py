# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
if __name__=="__main__":
    a = 8
    l = [2,3,5]
    z = a//2
    while z != 2:
        if z in l:
            break
    print(z)

