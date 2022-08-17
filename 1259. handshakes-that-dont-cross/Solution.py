# https://leetcode.com/problems/handshakes-that-dont-cross

class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        global d
        d= {1:1}
        def rec(low, up):
            global d
            if(up-low in d): return d[up-low]
            aux = rec(low+2, up) + rec(low+1, up-1)
            for i in range(low+3, up-1, 2):
                left = rec(low+1, i-1)
                right = rec(i+1, up)
                aux+= left*right
                aux = aux%(10**9 + 7)
            d[up-low] = aux
            return aux
        return rec(1, numPeople)