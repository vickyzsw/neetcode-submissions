class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for i in range(len(strs)):
            a += str(len(strs[i])) + "#" + strs[i]
        return a
    def decode(self, s: str) -> List[str]:
        word =[]

        while len(s) > 0:
            length = 0
            n=0
            for i in s:
                if i == "#":
                    break   
                else: 
                    length = length*10 + int(i)
                    n += 1
            word.append(s[n+1:length+n+1])
            s = s[length + n + 1 :]
        return word
            