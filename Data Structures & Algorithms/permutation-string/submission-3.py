class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        baseline = self.getFreqCount(len(s1), s1, 0)
        freqCount = self.getFreqCount(len(s1), s2, 0)

        if baseline == freqCount:
            return True

        for i in range(len(s1), len(s2)):
            letter = s2[i]
            if letter in freqCount:
                freqCount[letter] += 1
            else:
                freqCount[letter] = 1
            
            oldLetter = s2[i - len(s1)]
            freqCount[oldLetter] -= 1
            if freqCount[oldLetter] == 0:
                del freqCount[oldLetter]

            if baseline == freqCount:
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