f = open("C:\\Users\\vishatha\Desktop\\New folder (6)\\test.txt","r")
# print(f.read())
ll = []
for x in f.read().split(" "):
    ll.append(x)

print(ll)
print(set(ll))
