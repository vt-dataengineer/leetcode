#911-->8111 44->1616 203->409

a = 203
s = str(a)
l = []

print(s)
for x in s:
    z = int(x)*int(x)
    #print(str(z),end='')

print(bin(32)+"\n")
binn = bin(31)
binn = binn.split('b')
z = str(binn[1])
count = 0
for c in z:
    if c == '1':
        count+=1
print(count)

