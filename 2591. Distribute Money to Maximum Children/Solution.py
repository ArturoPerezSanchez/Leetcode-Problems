# https://leetcode.com/problems/distribute-money-to-maximum-children

class Solution:
    def distMoney(self, money, children):
        if money < children: return -1
        ch = [1]*children
        money-=children
        aux = 0
        for i in range(len(ch)):
            if(money < 7): break
            ch[i] = 8
            aux+=1
            money-=7
        else:
            if(money == 0): return children
            return children -1
        if(aux == 0): return 0
        if(money != 3): return aux
        
        if(aux == children-1): return children -2
        return aux
        
        