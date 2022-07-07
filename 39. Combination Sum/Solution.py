# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []

        def solve(c, t, sol):
            if(t == 0):
                solutions.append(list(sol))
            else:
                for i in c:
                    if(i<=t and (not sol or i>=sol[-1])):
                        sol.append(i)
                        solve(c, t-i, sol)
                        sol.pop()


        solve(candidates, target, [])

        return solutions

            
        