class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord("a")] += 1
            key = tuple(count)
            h[key].append(s)
        return [val for key, val in h.items()]
        
