# https://leetcode.com/problems/generate-parentheses

class Solution:
    def selecciona(self,curr,abrir,cerrar,abrirocerrar,res):
        if(abrirocerrar):
            abrir-=1
            cerrar+=1
            curr += "("
        else:
            cerrar-=1
            curr +=")"

        if(abrir == 0 and cerrar == 0):
            res.append(curr)
        else:
            if(abrir>0):
                self.selecciona(curr,abrir,cerrar,True,res)
            if(cerrar>0):
                self.selecciona(curr,abrir,cerrar,False,res)
        return res
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        return self.selecciona("",n,0,True,[])

