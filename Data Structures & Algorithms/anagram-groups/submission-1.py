class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            counter = [0] * 26
            for letter in word:
                counter[ord(letter) - ord("a")] += 1
            use = tuple(counter)
            dic[use].append(word)
        return [v for k, v in dic.items()]

