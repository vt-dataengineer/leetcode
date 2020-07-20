# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

nums = [-1,0,3,5,9,12]
target = 9

left = 0
right = len(nums)-1

while left<=right:
    pivot = left+(right-left)//2
    #print(pivot)
    if nums[pivot]==target:
        print(pivot)
    if target<nums[pivot]:
        right = pivot-1
    else:
        left = pivot+1
