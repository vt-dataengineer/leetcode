# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
if __name__=='__main__':
    s = 'a'
    s1 = 'b'
    if s in s1:
        print('True')
    else:
        print("False")
