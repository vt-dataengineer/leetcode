import  random
# name = input("Enter name: ")
# age = input("Enter age: ")
# print("Name : "+name.upper()+" Age: "+str(int(age)+100))

print(random.randint(1,100))
def add(n):
    return n+n

b = [1,2,3,4]
a = map(add,b)
print(list(a))

z = map(lambda x:x*x,b)
print(list(z))
