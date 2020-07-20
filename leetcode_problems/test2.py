import pandas as pd
if __name__ == '__main__':
    # s = '  Vishal'
    # if(s.__contains__('')):
    #     print("Spaces")
    # print(s[::-1])
    # print(s.upper())
    # print(s.split('a'))
    # print(len(s))
    # print(s*2)
    # for x in s:
    #     print(x)
    #
    # for y in range(0,len(s)):
    #     print(str(y)+"th Element "+s[y])

    # di = {1:'one',2:"two",3:"three"}
    # for x,y in di.items():
    #     print(str(x)+"==>"+str(y))

    # li = ('la','b','c','d','e','f')
    # for x in li:
    #     print(x)
    # print(len(li))
    f = open("C:\\Users\\vishatha\Desktop\\test\\file1.txt","r")
    #print(f.read())
    df1 = pd.read_csv(r'C:\\Users\\vishatha\Desktop\\test\\file1.txt')
    print(df1)
    filter = df1['AGE']>30
    print(df1.where(filter))
    print(df1.where(df1['NAME']=='Harshul'))
    print(df1.size)


    # df = pd.DataFrame(f,columns = ['id','name','age'])
    # print(df)
