# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
if __name__=='__main__':
    s = '3[a]2[bc]'
    st = ''
    s.replace('[','')

    st = s.replace('[','').replace(']','')
    print(st)

    for x in st:

