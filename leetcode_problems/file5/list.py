a = {1:'yes'}
# print(a)
a[2]='no'
# print(a)
# print(a[1])
while(1):
    ch = int(input("enter choice: \n 1: new entry \n 2: View all \n 3: Stop \n"))
    if ch == 1:
        key = input('Enter key: ')
        value = input('Enter value: ')
        a[key] = value
    elif ch == 2:
        print(a)
    elif ch == 3:
        break

