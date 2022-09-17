# https://leetcode.com/problems/4-keys-keyboard

class Solution:
    # def maxA(self, n):
    #     if n<=6: return n
    #     if n==7: return 9
    #     if n==8: return 12
    #     if n==9: return 16
    #     if n==10: return 20
    #     if n==11: return 27
    #     if n==12: return 36
    #     if n==13: return 48
    #     if n==14: return 64
    #     if n==15: return 81
    #     if n==16: return 108
    #     if n==17: return 144
    #     if n==18: return 192
    #     if n==19: return 256
    #     if n==20: return 324
    #     if n==21: return 432
    #     if n==22: return 576
    #     if n==23: return 768
    #     if n==24: return 1024
    #     if n==25: return 1296
    #     if n==26: return 1728
    #     if n==27: return 2304
    #     if n==28: return 3072
    #     if n==29: return 4096
    #     if n==30: return 5184
    #     if n==31: return 6912
    #     if n==32: return 9216
    #     if n==33: return 12288
    #     if n==34: return 16384
    #     if n==35: return 20736
    #     if n==36: return 27648
    #     if n==37: return 36864
    #     if n==38: return 49152
    #     if n==39: return 65536
    #     if n==40: return 82944
    #     if n==41: return 110592
    #     if n==42: return 147456
    #     if n==43: return 196608
    #     if n==44: return 262144
    #     if n==45: return 331776
    #     if n==46: return 442368
    #     if n==47: return 589824
    #     if n==48: return 786432
    #     if n==49: return 1048576
    #     if n==50: return 1327104


    # Recursive Solution
    def maxA(self, n: int) -> int:
        if n<=3: return n
        global res
        res = 0

        @cache
        def rec(remainingMoves, copied, currentScore):
            if(remainingMoves == 0):
                global res
                res = max(res, currentScore)
                return
            if(copied>0): rec(remainingMoves-1, copied, currentScore+copied)
            else: rec(remainingMoves-1, copied, currentScore+1)
            
            if(remainingMoves>2): rec(remainingMoves-3, currentScore, currentScore*2)
        

        rec(n-3, 0, 3)
        return res



            
