import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for st in strs:
            cur = [0] * 26
            for letter in st:
                pos = ord(letter) - ord('a')
                cur[pos] += 1
                
            hs = tuple(cur)
            if hs in data:
                data[hs].append(st)
            else:
                data[hs] = [st]

        final = []
        for key in data.keys():
            final.append(data[key])
        
        return final
