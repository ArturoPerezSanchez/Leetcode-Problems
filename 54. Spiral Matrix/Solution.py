# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        firstR = 0
        lastR = len(matrix)-1
        firstC = 0
        lastC = len(matrix[0])-1
        '''
            1
            ^
        0 <-+-> 2
            |
            3
        '''

        mov = 2
        currentR = 0
        currentC = 0
        if(lastC == 0):
            for i in matrix:
                res.append(i[0])
            return res
        elif(lastR == 0):
            return matrix[0]

        while(firstR!=lastR and firstC!=lastC):
            res.append(matrix[currentR][currentC])
            if(mov==2):
                currentC +=1
                if(currentC == lastC):
                    mov = 3
                    firstR +=1
                    continue
            if(mov == 3):
                currentR +=1
                if(currentR == lastR):
                    mov = 0
                    lastC -=1
                    continue
            if(mov == 0):
                currentC-=1
                if(currentC == firstC):
                    mov = 1
                    lastR -=1
                    continue
            if(mov == 1):
                currentR -=1
                if(currentR == firstR):
                    mov = 2
                    firstC +=1
                    continue

        res.append(matrix[currentR][currentC])
        if(mov==0):
            currentC -=1
            mov=1
        elif(mov==1):
            mov =2 
            currentR -=1
        elif(mov==2):
            mov = 3
            currentC +=1
        elif(mov==3):
            mov = 0
            currentR +=1

        if(firstC!=lastC):
            if(mov == 2):
                while(currentC != lastC):
                    res.append(matrix[currentR][currentC])
                    currentC +=1
            else:
                while(currentC != firstC):
                    res.append(matrix[currentR][currentC])
                    currentC -=1
        else:

            if(mov == 1):
                while(currentR != firstR):
                    res.append(matrix[currentR][currentC])
                    currentR -=1
            else:
                while(currentR != lastR):
                    res.append(matrix[currentR][currentC])
                    currentR +=1
        res.append(matrix[currentR][currentC])
        return res
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    