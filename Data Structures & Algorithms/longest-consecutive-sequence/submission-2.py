class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = set(nums)

        final = 0
        for num in nums:
            # Not start
            if num - 1 in hm:
                continue

            # Start of sequence
            total = 1
            while num + 1 in hm:
                total += 1
                num += 1

            final = max(final, total)

        return final
