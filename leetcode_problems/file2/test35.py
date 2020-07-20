# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
if __name__=='__main__':
    num = 232
    target = 6
    a = []
    op = ['+','-','*']
    for x in str(num):
        a.append(int(x)%10)
    print(a)

    for y in a:
        if y+y ==target or y*y == target or y-y == target:
            print(y)


