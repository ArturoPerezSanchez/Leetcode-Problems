# https://leetcode.com/problems/basic-calculator-ii

class Solution:

    def calculate(self, s: str) -> int:
        aux = ""
        currentNumber = ""
        i = -1
        while i < len(s)-1:
            i+=1
            if(s[i] == " "): continue
            if(s[i].isdigit()):
                currentNumber += s[i]
            else:
                if(s[i] == "+" or s[i] == "-"):
                    aux+=currentNumber + s[i]
                    currentNumber = ""
                else:
                    currentNumber = int(currentNumber)
                    nextNumber = ""
                    op = s[i]
                    for j in range(i+1, len(s)):
                        if(s[j] not in ["+", "-", "*", "/"]):
                            nextNumber += s[j]
                        else:
                            i = j-1
                            break
                    else:
                        i = j
                    nextNumber = int(nextNumber)
                    if(op == "*"):
                        currentNumber = str(currentNumber * nextNumber)
                    else:
                        currentNumber = str(int(currentNumber / nextNumber))
                    
        aux+=currentNumber

        currentNumber = ""
        i = 0

        while(i<len(aux)):
            if(aux[i] == " "): continue
            
            if(aux[i].isdigit()):
                currentNumber += aux[i]
            else:
                op = aux[i]
                
                currentNumber = int(currentNumber)
                nextNumber = ""
                for j in range(i+1, len(aux)):
                    if(aux[j] not in ["+", "-"]):
                        nextNumber += aux[j]
                    else:
                        i = j-1
                        break
                else:
                    i = j
                nextNumber = int(nextNumber)
                if(op == "+"):
                    currentNumber = str(currentNumber + nextNumber)
                else:
                    currentNumber = str(int(currentNumber - nextNumber))

            i+=1

        return int(currentNumber)



