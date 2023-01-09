# https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        carry, x10, res = 0, 0, 0
        for i in reversed(num2):
            val = "0"*x10
            for j in reversed(num1):
                carry, mul = divmod(int(i)*int(j) + carry, 10)
                val = str(mul) + val
            if(carry != 0):
                val = str(carry) + val
                carry = 0
            res += int(val)
            x10 +=1
        return str(res)
            
            
            