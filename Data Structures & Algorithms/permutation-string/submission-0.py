
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2  = len(s2)
        counter1 = [0] * 26
        counter2 = [0] * 26
        if n1 > n2:
            return False
        for i in range(n1):
            counter1[ord(s1[i]) - 97] += 1
            counter2[ord(s2[i]) - 97] += 1

        if counter1 == counter2:
            return True
        for i in range(n1,n2):
            counter2[ord(s2[i]) - 97] +=1
            counter2[ord(s2[i-n1]) -97] -=1
            if counter1 == counter2:
                return True
        return False


