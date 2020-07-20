if __name__ == '__main__':
    def climbStairs(n):
        l = [1,2]
        count = 0

        if l[0]+l[1]==n:
            count+=1
            l[0]=l[1]
            print('***'+str(l[0]))

        print(count)


print(climbStairs(3))
