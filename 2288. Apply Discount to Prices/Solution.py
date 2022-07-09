# https://leetcode.com/problems/apply-discount-to-prices

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        discountMult = (100-discount)/100
        res = ""
        i=0
        while (i <len(sentence)):
            if (sentence[i] == "$" and (i== 0 or sentence[i-1] == " ")):
                word = 0
                for j in range(i+1, len(sentence)):
                    if(sentence[j] == " "):
                        break
                    else:
                        word+=1
                aux = sentence[i+1:i+1+word]
                if(aux.isdigit()):
                    res += "${:.2f}".format(int(aux)*discountMult)
                else:
                  res += sentence[i:i+1+word]
                i+=word
            else:
              res += sentence[i]
            i+=1 
        return res