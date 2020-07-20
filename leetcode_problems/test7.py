if __name__ == '__main__':
    dry = {"I":1,
           "V":5,
           "X":10,
           "L":50,
           "C":100,
           "D":500,
           "M":1000}
    # for k,v in dry.items():
    #     print(k,v)

    def roman(t):
        s = 0
        for x in range(0,len(t)):
            if t[x] in dry:
                if x+1 < len(t):
                    if dry[t[x]] < dry[t[x+1]]:
                        z = dry[t[x+1]]-dry[t[x]]
                        s = s+z
                    else:
                        s = s + dry[t[x]]
                # else:
                #     s = s+dry[t[x]]
        print(s)

    v = input("Enter roman: ").upper()
    roman(v)
