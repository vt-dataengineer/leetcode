l1 = 'v'
l2 = 'l'
test_list = []
alpha = 'a'
for i in range(0, 26):
    test_list.append(alpha)
    alpha = chr(ord(alpha) + 1)

print(str(test_list))

# for a in range(len(test_list)):
#     for b in range(len(test_list)):
#         for c in range(len(test_list)):
#             for d in range(len(test_list)):
#                 for e in range(len(test_list)):
#                     for f in range(len(test_list)):
#                         if l1+test_list[a]+test_list[b]+test_list[c]+test_list[d]+ test_list[e]+ test_list[f]+l2 == 'vishal':
#                             print('True')
#                         # print(l1+test_list[a]+test_list[b]+test_list[c]+test_list[d]+ test_list[e]+ test_list[f]+l2)
#
def ff(l):
    s = 1
    for a in range(len(l)-1):
        for b in range(len(l)-1):
            print(l1+l[a]+l[s]+l2)
        s +=1


ff(test_list)



# q = 0
# def ff(l):
#     for a in range(len(l)):
#         return l[a]
#
# def ff1(ll):
#     for b in range(len(ll)):
#         print(l1 + ' ' + ll[b]+ ff(ll) + ' ' + l2)
#
# ff1(test_list)
