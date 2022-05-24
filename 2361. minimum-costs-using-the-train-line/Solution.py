# https://leetcode.com/problems/minimum-costs-using-the-train-line

class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:

        res = []
        inExpress = False
        currentSum = 0
        expressRoute = expressCost
        for i in range(len(regular)):
            exp = express[i]
            expressRoute += exp
            if(not inExpress): exp+=expressCost

            if(currentSum+exp<expressRoute): expressRoute = currentSum+exp
            else: exp = expressRoute-currentSum
            
            if(regular[i]<exp):
                currentSum += regular[i]
                inExpress = False
            else:
                currentSum += exp
                inExpress = True
            res.append(currentSum)
        return res