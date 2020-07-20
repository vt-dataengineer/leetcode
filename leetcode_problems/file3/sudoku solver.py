grid =    [[3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]]

# for x in range(0,len(grid)):
#     print(grid[x])
#
cube1 = []
for x in range(0,3):
    a = []
    for y in range(0,3):
        print(str(grid[x][y]))
        a.append(str(grid[x][y]))
    cube1.append(a)
# cube1 = list(str(grid[1]).
print(cube1)
for x in cube1:
    print(x)

