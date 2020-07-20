# Input: 38
# Output: 2
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
#              Since 2 has only one digit, return it.
if __name__=='__main__':
    def iam(c):
        a = 0
        if len(str(c)) ==1:
            print(str(c))
        else:
            x = c // 10
            y = c % 10
            a = x+y
            iam(a)
iam(45)
