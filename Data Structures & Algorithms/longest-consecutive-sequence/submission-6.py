class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = sorted(nums)

        current = 1
        longest = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] - 1:
                current += 1
            elif nums[i] == nums[i + 1]:
                continue
            else:
                current = 1

            longest = max(longest, current)

        return longest
