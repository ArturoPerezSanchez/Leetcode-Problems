# https://leetcode.com/problems/remove-k-digits

class Solution:
    # Solution 1: Using a stack
    def removeKdigits(self, num: str, k: int) -> str:
        if(k>=len(num)): return "0"
        stack = []
        for d in num:
            # remove sequences of decending numbers first
            while stack and d < stack[-1] and k:
                stack.pop()
                k -= 1

            # add digit to the stack unless it would be a leading 0
            if stack or d != '0':
                stack.append(d)
       
        # if you're left with only ascending digits, then remove the remaining 
        # k elements from the back of the list (the largest digits)
        if k: stack = stack[:-k]

        # return '0' instead of an empty string
        if len(stack) == 0: return '0'
        return ''.join(stack)

    # Solution 2: using recursion
    def removeKdigitsRecursive(self, num: str, k: int) -> str:
        if(k>=len(num)): return "0"
        def rec(n, k, res):
            if(k == 0): return res+n
            current = int(n[0])
            for i in range(1,len(n)):
                if(int(n[i]) < current):
                    return rec(n[:i-1] + n[i:], k-1, res)
                current=int(n[i])
            res += n[:-k]
            return res
        res = rec(num,k,"")
        return str(int(res))


