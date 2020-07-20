# Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].
#
# Output: 4
#
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
#              After finishing it you will obtain profit 1 and your capital becomes 1.
#              With capital 1, you can either start the project indexed 1 or the project indexed 2.
#              Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
#              Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

if __name__=='__main__':
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,1]

    d = dict(zip(profits,capital))
    print(d)


    # for x in range(len(capital)):
    #     w+=profits[capital[x]]
    #     print(w)

