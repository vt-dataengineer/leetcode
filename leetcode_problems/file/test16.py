# Input: "the sky is blue"
# Output: "blue is sky the"
if __name__ == '__main__':
    s = 'the sky is    blue'
    l = len(s)
    print(l)

    # print(s.strip())
    # print(s.replace(" ", ""))
    j = " ".join(s.split())
    print(j)

    re = j.split(' ')
    rev = re[::-1]
    sp =' '
    print(sp.join(rev))

