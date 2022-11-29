# https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        gamesLosts = {}
        ans1 = []
        ans2 = []

        for winner, looser in matches:
            if winner not in gamesLosts: gamesLosts[winner] = 0
            if looser not in gamesLosts: gamesLosts[looser] = 1
            else: gamesLosts[looser] +=1

        for i, j in gamesLosts.items():
            if(j == 0): ans1.append(i)
            if(j == 1): ans2.append(i)

        return [sorted(ans1), sorted(ans2)]
