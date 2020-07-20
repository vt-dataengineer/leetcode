# Input: nums = [1,2,2,4]
# Output: [2,3]

nums = [2,2,]
op = []
# ss = sorted(nums)
# if ss == nums:
for x in range(len(nums)-1):
   if nums[x]==nums[x+1]:
       if len(nums)==2:
            op.append(nums[x])
            op.append(nums[x]-1)
       else:
           op.append(nums[x])
           op.append(nums[x] + 1)

print(op)
# else:
#     for x in range(len(nums)-1):
#         if nums[x]==nums[x+1]:
#             op.append(nums[x])
#             op.append(nums[x]-1)
#     print(op)
# for x in range(len(nums)-1):
#     if nums[x]==nums[x+1]:
#         print(nums[x]-1)
#         print(nums[x])





