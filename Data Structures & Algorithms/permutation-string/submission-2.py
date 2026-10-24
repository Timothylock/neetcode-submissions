class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        baseline = self.getFreqCount(len(s1), s1, 0)

        for i in range(0, len(s2) - len(s1) + 1):
            if self.getFreqCount(len(s1), s2, i) == baseline:
                return True
        
        return False


        
    def getFreqCount(self, length, s, pos) -> dict:
        ret = {}
        for i in range(pos, pos + length):
            if s[i] in ret:
                ret[s[i]] += 1
            else:
                ret[s[i]] = 1
        
        return ret