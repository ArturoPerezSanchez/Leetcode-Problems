# https://leetcode.com/problems/coin-change

class Solution:

    # Solution1: using recursive function and storing the necesary coins for each amount in a dictionary
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {0:0}
        def rec(amount):
            if (amount<0): return -1
            if (amount in d): return d[amount]
            res = -1
            for i in coins:
                aux = rec(amount-i)
                if(aux>=0 and (res==-1 or aux<res)):
                    res = aux+1
            d[amount] = res
            return res
        return rec(amount)

    # Solution 2: Using cache decorator
    def coinChange2(self, coins: List[int], amount: int) -> int:
        @cache
        def rec(amount):
            if (amount<0): return -1
            if (amount==0): return 0
            res = -1
            for i in coins:
                aux = rec(amount-i)
                if(aux>=0 and (res==-1 or aux<res)): res = aux+1
            return res
        return rec(amount)

    # Solution 3: Using cache decorator and only 1 function
    def coinChange3(self, coins: List[int], amount: int) -> int:
        if (amount<0): return -1
        if (amount==0): return 0
        res = -1
        for i in coins:
            aux = self.coinChange(coins, amount-i)
            if(aux>=0 and (res==-1 or aux<res)): res = aux+1
        return res