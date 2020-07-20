# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

l = 1
r = 22
ll = []
for x in range(l,r+1):
    if len(str(x)) == 1:
        print(x)
    if len(str(x))>1 and str(x).__contains__('0'):
        continue
    if len(str(x))>1:
        for y in str(x):
            if int(x)%int(y) == 0:
                print(x,y)

print(set(ll))


