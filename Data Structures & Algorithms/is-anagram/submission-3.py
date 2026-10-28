class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        a=0
        for i in s:
            if i in count_s:
                count_s[i] += 1
            else:
                count_s[i] = 1
        for n in t:
            if n in count_t:
                count_t[n] +=1
            else:
                count_t[n] = 1
        if len(s) != len(t):
            return False

        for m in count_s:
            if m not in count_t:
                return False
            if count_s[m] != count_t[m]:
                return False
        return True

                
