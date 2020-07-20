if __name__ == '__main__':
    nums = [2,11,5,3,15,8]
    numss = [-1,0,1,2,-1,-4]
    target = 10

    # for x in range(0,len(nums)-1):
    #     for y in range(0,len(nums)-1):
    #         if nums[x]+nums[y+1] == target:
    #             print(str(x),str(y+1))



    for a in range(0,len(numss)-1):
        for b in range(0,len(numss)-1):
            if numss[a]+numss[b+1] == 0:
                print(str(numss[a]),str(numss[b+1]))
                #print(str(a),str(b+1))
