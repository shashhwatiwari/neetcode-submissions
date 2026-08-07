class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for i in range(0,n+1)]
        def memoisedStairs(n):
            if n == 0:
                return 0
            else:
                if memo[n] != 0:
                    return memo[n]
                else:
                    if n == 2:
                        memo[n] = 2
                        return memo[n]
                    elif n == 1:
                        memo[n] = 1
                        return memo[n]
                    else:
                        memo[n] = memoisedStairs(n-1) + memoisedStairs(n-2)
                        return memo[n]
        return memoisedStairs(n)
        
        