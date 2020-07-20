# Input: "leetcode"
# Output: "leotcede"
if __name__=='__main__':
    s = 'leetcode'
    vow = ['a','e','i','o','u']
    for x in s:
        if x in vow:
            print(x)

