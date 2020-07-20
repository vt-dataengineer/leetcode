# Input:
# ["a","a","b","b","c","c","c"]
#
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


l = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
d = {}
st = []
# s = list(set(l))
# print(s)
# print(l)
# for x in s:
#     print(l.count(x))
if len(l) == 1:
    st.append('1')
    print(st)
else:
    for x in l:
        d.update({x:l.count(x)})
        #print(x,l.count(x))
    #print(d)
    for k,v in d.items():
        #print(k,v,end=' ')
        st.append(k)
        if len(str(v))>1:
            for y in str(v):
                st.append(str(y))
    print(st)

