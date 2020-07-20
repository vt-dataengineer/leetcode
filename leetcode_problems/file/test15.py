if __name__ == '__main__':
    # Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # Output: 49
    l = [1,8,6,2,5,4,8,3,7]
    m = max(l)
    print(m)
    add = 0
    for x in l:
        if x < m:
            i = l.index(x)
            add = add + l[i]
            print(i)
    print(add)


    # for i in range(len(l)):
    #     for j in range(i+1,len(l)):
    #         if l[i]==7 and l[j]==7:
    #             ar = l[i]*l[j]
    #             print(ar)








