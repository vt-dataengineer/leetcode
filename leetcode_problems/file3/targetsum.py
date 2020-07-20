#Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

if __name__=="__main__":
    nums = [1, 1, 1, 1, 1]
    s = 3
    sum = ''

    op = ['+','-']
    for x in range(len(nums)):
        sum+= op[0]+str(nums[x])
        if eval(sum) == s:
            print(sum)

        #print(eval(str(nums[x])+op[0]+str(nums[x+1])))
    #print(eval(str(x)+op[0]+str(x)))
