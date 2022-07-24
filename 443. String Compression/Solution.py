# https://leetcode.com/problems/string-compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        aux = deque(chars)
        currentCharacter = chars[0]
        counter = 0
        for i in range(len(chars)):
            c =aux.popleft()
            if(c == currentCharacter): counter+=1
            else:
                aux.append(currentCharacter)
                if (counter != 1):
                    for i in str(counter):
                        aux.append(i)
                    counter = 1
                currentCharacter = c

        aux.append(currentCharacter)
        if(counter!=1):
            for i in str(counter):
                aux.append(i)
        chars[:] = list(aux)[:]