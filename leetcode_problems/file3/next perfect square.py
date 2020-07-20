#find next perfect square
#25->36,81->100,40-->-1

a = 80
z = 0
for x in range(1,a):
    if a//x == x:
        z = x

print((z+1)*(z+1))
