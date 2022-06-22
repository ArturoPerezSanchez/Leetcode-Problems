class Solution:
    def convert(self, s: str, numRows: int) -> str:
        count = 0            # Initialize a counter variable 'count' to 0
        res = ['']*numRows   # Create a list 'res' with 'numRows' empty strings
        dsc = False          # Initialize a boolean variable 'dsc' to False
        
        # Loop through each character 'i' in the input string 's'
        for i in s:
            # If the counter is greater than or equal to numRows - 1, Set the boolean variable 'dsc' to True
            if(count>=numRows-1):    
                dsc = True
            # If the counter is less than or equal to 0, Set the boolean variable 'dsc' to False          
            elif(count<=0):
                dsc = False

            # Add the current character 'i' to the 'count'-th element of 'res'      
            res[count] += i
            
            # If 'dsc' is True Decrement the counter variable 'count', if not increment the counter variable 'count'
            if(dsc):
                count -=1
            else:    
                count +=1

        # Return the concatenated string of elements in 'res'
        return ''.join(res)    
