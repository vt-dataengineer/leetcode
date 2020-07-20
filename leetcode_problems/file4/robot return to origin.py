# Input: "UD"
#The move sequence is represented by a string, and the character moves[i] represents its ith move.
# Valid moves are R (right), L (left), U (up), and D (down).
# If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
# Output: true
# Explanation: The robot moves up once, and then down once.
# All moves have the same magnitude, so it ended up at the origin where it started.

s = 'LRUD'
y = 0
z = 0
for x in s:
    if x == 'U':
        y+=1
    elif x == 'D':
        y-=1
    elif x == 'L':
        z+=1
    elif x == 'R':
        z-=1
if y == z:
    print('True')
else:
    print('False')

