if __name__=='__main__':
    t = 'appliance'
    s = 'alan'
    t1 = list(t)
    s1 = list(s)
    l =[]
    print(t1)
    print(s1)
    # for x in range(len(t1)):
    #     if s1.index(t1[x])<s1.index((t1[]))
    # for a in s:
    #     if a in t:
    # for x in range(0,len(s1)-1):
    #         if s1[x] in t1:
    #
    #             print('True')
    #         else:
    #             print('False')
    for x in range(len(s1)):
        #print(s1.index(s1[x]))
        print(t1.index(s1[x]))
        l.append(t1.index(s1[x]))
    print(l)
    if l == sorted(l):
        print('True')
    else:
        print('False')

        # if t1.index(s1[x])<t1.index(s1[x+1]):
        #     print('True')

        # if s1.index(s1[x])<s1.index(t1[x]):
        #     print('True')
        # else:
        #     print('False')
        #



