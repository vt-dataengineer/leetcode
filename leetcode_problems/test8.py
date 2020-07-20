if __name__ == '__main__':
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print(nums)



    l = [-1, 0, 1, 2, -1, -4]
    print(l)

    for x in range(0,len(l)-1):
        for j in range(0,len(l)-1):
            if l[x]+l[j+1] == 0:
                print('true')

