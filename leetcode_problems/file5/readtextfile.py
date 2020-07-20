def email(s):
    f = open("C:\\Users\\vishatha\Desktop\\test.txt", "r")
    d = dict()
    for x in f:
        d[x.split(':')[0]] = x.split(':')[1].rstrip('\n')
    if s in d:
        return d[s]
    else:
        return 'not a valid name'



print(email('bhishaj'))
print(email('vishal'))
l = [1,2,3,4,5]
print([x for x in l if x>2])
y = lambda z: z*z
print(y(2))
