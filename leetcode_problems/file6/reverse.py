# l = ['vishal','thakur','is','my','name']
#
# # l.reverse()
# # print(l)
# # print(list(reversed(l)))
#
#
# ll =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#
# ll.sort(key=lambda x: x[1])
# print(ll)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for x in range(6):
#     for y in range(1,x+1):
#         print(y,end = ' ')
#     print('')


# [1,2,3] -> [2,3,1]

# l = [1,2,3]
#
# print(l[1:]+l[:1])
# 1 2 3 4 5

n = int(input())
if n==1:
    print(1)
elif(n==2 or n==3):
    print('No solution')
else:
    for i in range(2,n+1,2):
        print(i,end=' ')
    for i in range(1,n+1,2):
        print(i,end= ' ')


