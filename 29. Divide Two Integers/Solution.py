# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:   
        if dividend == 0 :  return 0
        if dividend > 2**31-1 : return 2**31-1
        if dividend < - 2**31 : return -2**31
        if divisor ==  1 : return min(2**31-1, max(-2**31, dividend))
        if divisor == -1 : return min(2**31-1, max(-2**31, -dividend))
        
        sign = 1 if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) else -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        string_dividend = str(dividend)
        res = ''
        x = ''
        while string_dividend:
            x += string_dividend[0]
            temp_res = 0
            while int(x) >= divisor:
                temp_res+=1 
                x = str(int(x) - divisor)
            
            res += str(temp_res)
            string_dividend = string_dividend[1:]
                    
        res = int(res)*sign
        return res