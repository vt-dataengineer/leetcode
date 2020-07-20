

def ana(s,s1):
    for x in s:
        if x in s1 and len(s)==len(s1):
            return True
        else:
            return False

s = 'hello'
s1 = 'ollehnnk'
print(ana(s,s1))
