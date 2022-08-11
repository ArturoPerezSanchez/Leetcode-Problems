class Solution:

    # Using 2 pointers
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        
        for i in range(len(x)//2):
            if (x[i] !=x[-i-1]): return False

        return True
    
    # Creating the reversed string and comparing
    def isPalindrome2(self, x: int) -> bool:
        if(x<0): return False
        x = str(x)
        return x == x[::-1]