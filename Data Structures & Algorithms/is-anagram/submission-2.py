class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}

        for char in s:
            count1[char] = count1.get(char,0) + 1

        for char in t:
            count2[char] = count2.get(char,0) + 1 #.get(char,0)+1 will take the current count and add 1 to it, if its new it is zero

        return count1 == count2