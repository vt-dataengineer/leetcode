# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
if __name__=='__main__':
    s = 'leetcode'
    st = ''
    for x in s:
        if x in st:
            break
        else:
            st = st+x
    print(st)
