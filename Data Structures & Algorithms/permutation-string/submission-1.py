class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2 :
            return False
        
        for i in range(n1):
            counter1[s1[i]] += 1
            counter2[s2[i]] += 1
        
        if counter1 == counter2:
            return True
        
        #abc
        #lecabee

        for i in range(n1, n2):
            counter2[s2[i - n1]] -= 1
            if counter2[s2[i - n1]] == 0:
                del counter2[s2[i-n1]]
            counter2[s2[i]] += 1
            if counter1 == counter2:
                return True
            print(counter1, counter2)
        return False