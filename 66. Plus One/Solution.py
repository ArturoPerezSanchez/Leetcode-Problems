# https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        carry = True
        ind = len(digits)-1
        while(carry):
            if(ind < 0):
                digits.insert(0, 1)
                break
            if(digits[ind] != 9):
                digits[ind] += 1
                carry = False
            else:
                digits[ind] = 0
                ind = ind -1

        return digits
            
            
            
        