#Input: 5
#Output: 2
#Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

if __name__ == '__main__':
    a = 5
    one = ''
    def convert(y):
        return '1' if (y=='0') else '0'
    #print("{0:b}".format(a))
    comp = bin(a)
    #print(comp)
    sp = comp.split('b')
    #print(sp[1])
    for x in sp[1]:
        one+=convert(x)

    #print(one)
    print(int(one,2))





