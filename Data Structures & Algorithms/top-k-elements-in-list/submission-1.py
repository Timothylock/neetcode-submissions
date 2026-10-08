class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        for num in nums:
            if num in numFreq:
                numFreq[num] += 1
            else:
                numFreq[num] = 1

        freqNum = {}
        for num in numFreq.keys():
            times = numFreq[num]
            if times in freqNum:
                freqNum[times].append(num)
            else:
                freqNum[times] = [num]

        allkeys = list(freqNum.keys())
        final = []
        while len(final) < k:
            highest = max(allkeys)
            allkeys.remove(highest)
            final += freqNum[highest]

        return final
            