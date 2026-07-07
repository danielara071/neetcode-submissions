class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n1 = len(word1)
        n2 = len(word2)
        pos1 = 0
        pos2 = 0
        count = 0
        turnWord1 = True
        while pos1 < n1 and pos2 < n2:
            if turnWord1:
                res.append(word1[pos1])
                pos1 +=1 
                turnWord1 = False
            else:
                res.append(word2[pos2])
                pos2 += 1
                turnWord1 = True
            count += 1
        if n1 < n2:
            res.append(word2[pos2::])
        elif n2 < n1:
            res.append(word1[pos1::])
        elif n2 == n1:
            res.append(word2[pos2::])

        return "".join(res)
