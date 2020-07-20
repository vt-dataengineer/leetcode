# 3
# 4 3
# 3 1 9 100
# 6 2
# 5 5 1 2 3 4
# 5 5
# 7 7 1 7 7

n = input()
tc = input()
skill = input()
length = len(skill.split())
# if length > int(tc.split()[0]):
#     print("Error in values")
# else:
print(n)
print(tc)
print(skill)
total_player = tc.split()[0]
player_to_choose = tc.split()[1]
print('Total: '+ total_player)
print('Player to choose : '+ player_to_choose)
ss = sorted(skill.split())
# print(ss)
ll = []
for x in ss:
    ll.append(int(x))


print(sorted(ll))


