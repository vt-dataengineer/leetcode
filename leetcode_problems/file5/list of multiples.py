# list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
ll = []
def list_of_multiples(x,y):
    for z in range(1,y+1):
        ll.append(x*z)

print(list_of_multiples(7,5))

print(ll)
