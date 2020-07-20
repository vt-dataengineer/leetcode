#numbers = "0123456789"
#lower_case = "abcdefghijklmnopqrstuvwxyz"
#upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#special_characters = "!@#$%^&*()-+"


if __name__=='__main__':
    s = 'aacabdddd23'
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    lo = ''
    up = ''
    num = ''
    move = 0

    if len(s)>=6 and len(s)<=20:
        for x in s:
            if x in lower_case:
                lo = lo+x
            elif x in upper_case:
                up = up+x
            elif x in numbers:
                num = num+x
        print(lo)
        print(up)
        print(num)
        if len(lo) == 0:
            print('Enter a lowercase')
        elif len(up)==0:
            print('Enter an uppercase')
        elif len(num)==0:
            print('Enter one numeric value')


    else:
        print('Short length')

