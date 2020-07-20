# Input: s = "anagram", t = "nagaram"
# Output: true
if __name__=='__main__':
    s = 'rat'
    t = 'car'

    if sorted(s)==sorted(t):
        print('True')
    else:
        print('False')

