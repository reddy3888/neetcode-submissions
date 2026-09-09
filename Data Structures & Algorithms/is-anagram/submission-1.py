class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}

        for char in s:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1

        for char in t:
            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1

        return count1 == count2