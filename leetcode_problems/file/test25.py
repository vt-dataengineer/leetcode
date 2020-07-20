# Input: 16
# Output: true
# Explanation: 24 = 16
if __name__=='__main__':
    a = 16
    for n in range(0,5):
        if pow(2,n) == a:
            print('True')
