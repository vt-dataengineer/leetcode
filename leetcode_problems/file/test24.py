# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
if __name__=='__main__':
    l = [3,2,3,1,2,4,5,5,6]
    #print(sorted(l))
    k = 6
    s = set(l)
    #print(s)

    final_list = []
    for num in l:
        if num not in final_list:
            final_list.append(num)
   # print(final_list)
    f = sorted(final_list)
    print(f[k-1])
    #print(str(k)+'th largest element : '+str(s[k]))

