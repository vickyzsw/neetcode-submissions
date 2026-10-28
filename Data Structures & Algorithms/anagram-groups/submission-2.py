class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            a = "".join(sorted(word))
            if a in group:
                group[a].append(word)
            if a not in group:
                group[a] = [word]
            
        return list(group.values())
    
