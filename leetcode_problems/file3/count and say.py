# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"

a = "1211"
c = []
for x in a:
    cc = a.count(x)
    print(x,cc)
    c.append(cc)
print(c)
print(list(a))

z = zip(c,list(a))
z = set(z)
print(z)
for k,v in z:
    print(str(k)+str(v),end='')

    #
    # print(str(x)+str(c))
