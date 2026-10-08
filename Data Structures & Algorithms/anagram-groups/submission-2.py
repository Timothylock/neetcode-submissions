import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for i in range(len(strs)):
            cur = [0] * 26
            for letter in strs[i]:
                pos = string.ascii_lowercase.index(letter)
                cur[pos] += 1
                
            hs = str(cur)
            
            if hs in data:
                data[hs].append(i)
            else:
                data[hs] = [i]

        final = []
        for key in data.keys():
            cur = []
            for i in data[key]:
                cur.append(strs[i])
            final.append(cur)
        
        return final
