# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def solve(digits, ans, out, ind, dic):
            if ind>=len(digits):
                ans.append(out)
                return
            val=dic[digits[ind]]
            for i in val:
                out+=i
                solve(digits, ans, out, ind+1, dic)
                out=out[:-1]

        ans=[]
        if len(digits)==0:
            return ans
        out=""
        ind=0
        dic={"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        solve(digits, ans, out, ind, dic)
        return ans
        