class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS, seenT = {}, {}
        for l in s:
            if l in seenS:
                seenS[l] += 1
            else:
                seenS[l] = 0

        for l in t:
            if l in seenT:
                seenT[l] += 1
            else:
                seenT[l] = 0

        return seenS == seenT