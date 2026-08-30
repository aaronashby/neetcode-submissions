class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []

        for s in strs:
            frequencies = [0 for i in range(26)]
            for char in s:
                frequencies[ord(char) - ord("a")] += 1
            
            anagrams[tuple(frequencies)].append(s)
        
        for group in anagrams.values():
            res.append(group)
        
        return res