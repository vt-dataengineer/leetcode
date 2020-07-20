# Input:
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.



# def one(a):
#     nums = [1, 7, 3, 6, 5, 6]
#     i = 1
#     s = 0
#     s1 = 0
#     for x in range(0,i):
#         s+=nums[x]
#         print(s)
#
#
#     for y in range(i,len(nums)):
#         s1+=nums[y]
#         print(s1)
#
#     if s == s1:
#         print('yes')
#     else:
#         print('No')
#         i+=1
#         one(i)
#
# one(1)

def one(i):
    nums = [1, 7, 3, 6, 5, 6]
    for x in range(i,len(nums)+1):








