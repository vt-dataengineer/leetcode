if __name__=='__main__':
    s = 'harshula'
    val = []
    for x in s:
        val.append(s.count(str(x)))
    d = dict(zip(val,list(s)))
    print(d)
    print('The maximum occured character is : '+str(d[max(d.keys())]))

