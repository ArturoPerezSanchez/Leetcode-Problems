class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a list of Roman numeral symbols for each digit place
        roms = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        # Compute the number of digits in the input number, multiplied by 2
        # This will be used to index into the roms list to get the symbols for each digit
        digits = len(str(num)) * 2

        # Initialize an empty list to hold the Roman numerals for each digit
        ans = []

        # Loop over each digit in the input number
        for i, val in enumerate(str(num), 1):
            # Compute the index of the current digit's Roman numeral symbols in the roms list
            digit = digits - 2 * i
            
            # If the current digit is 9, add the symbol for 9 and the symbol for 10^(digit+2)
            if val == '9': ans.extend([roms[digit], roms[digit+2]])


            # If the current digit is between 5 and 8, add the symbol for 5*10^digit and the symbol for 1*10^digit repeated (val-5) times
            if val in ['8', '7', '6', '5']: ans.extend([roms[digit+1], roms[digit] * (int(val) - 5)])
           
            # If the current digit is 4, add the symbol for 1*10^digit and the symbol for 5*10^digit
            if val == '4': ans.extend([roms[digit], roms[digit+1]])
            
            # If the current digit is between 1 and 3, add the symbol for 1*10^digit repeated val times
            if val in ['3', '2', '1', '0']: ans.extend([roms[digit] * int(val)])
        

        # Convert the list of Roman numerals for each digit to a single string and return it
        return ''.join(ans)