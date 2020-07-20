n = 105
# sum of adjacent digits shoud be = 1

ll = []
final = []
for x in range(10,n+1):
    ll.append([int(d) for d in str(x)])
# print(ll)

for y in ll:
    for z in range(len(y)):
        if y[z]-y[len(y)-1] == 1 or y[len(y)-1]-y[z] == 1:
            # print(y)
            final.append(y)


print(final)
