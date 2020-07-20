# Input: "cbacdcbc"
# Output: "acdb"
if __name__=='__main__':
    s = 'cbacdcbc'
    l = list(s)
    print(l)
    se = set(l)
    print(se)

    print(''.join(se))
