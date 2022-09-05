# https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for cur_idx, char in enumerate(s):
            if char == '(':
                stack.append(cur_idx)
            else:
                stack.pop()
                if not stack:  
                    stack.append(cur_idx)
                else:
                    max_len = max(max_len, cur_idx - stack[-1])
        return max_len