# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

if __name__=='__main__':
    a = 19
    b = str(a)
    #print(b)
    def f(a):
        b = str(a)
        # for x in range(len(b)-1):
        #     v = pow(int(b[x]),2) + pow(int(b[x + 1]),2)
        #     print(b[x]+' square + ' + b[x+1] + ' square = ' + str(v))
        #     if v == 1:
        #         print("true")
        #     else:
        #         f(v)
        for x in b:
                r = pow(int(x),2)
                print(r)




    # one = a//10
    # two = a%10
    # print(one,two)
#     def f(a):
#         one = a // 10
#         two = a % 10
#         val = (one * one) + (two * two)
#         print(str(one)+' square + '+str(two)+' square = '+str(val))
#         if val != 1:
#             return f(val)
#
#
#f(19)
