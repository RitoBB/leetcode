###########################动态规划###########################
################1. 找零钱💰#######################

def countWays(penny, n,aim):
    ## 1. 边界条件判断
    if n == 0 and aim > 1000 or aim < 1:
        return 0 
    ways = [0] * (aim+1)
    ways[0] = 1
    for i in range(n):
        for j in range(penny[i], aim +1):
            ways[j] = ways[j] + ways[j - penny[i]]
    return ways[aim]


def getMin(mmap, n,m):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = mmap[0][0]
    for i in range(1,m):
        dp[0][i] = mmap[0][i] + dp[0][i-1]
    for j in range(1,n):
        dp[j][0] == mmap[j][0] + dp[j-1][0]
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = mmap[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[i][j]

