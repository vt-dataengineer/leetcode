# Input: [3,30,34,5,9]
# Output: "9534330"
if __name__=='__main__':
    l = [3,30,34,5,9]
    t =[]
    for x in l:
        t.append(x%10)
    print(t)

    # t.sort(reverse=True)
    # print(t)
    # for i in t:
    #     if i in l:
    #         st = str()


    #print(sorted(l))

    d = dict(zip(t,l))
    #print(d)
    s =''

    for k,v in sorted(d.items(), reverse= True):
        print(k,v)
        s+=str(v)
    print(s)
