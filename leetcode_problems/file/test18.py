# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
if __name__=='__main__':
    nums = [1,2,3,1]
    for i in range(1,len(nums)-1):
        if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            ind = nums.index(nums[i])
    print(ind)
