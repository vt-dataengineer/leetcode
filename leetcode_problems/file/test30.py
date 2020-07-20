if __name__ == "__main__":
    s1 = '314592679238692376724626492098304986037'
    l = ['314','9860','767','01']
    c =0
    s = ""
    for x in l:
        if x in s1:
            c+=1
            print(x)
            s+=x+" "
    print(c)
    print(s)
