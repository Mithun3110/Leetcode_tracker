# Last updated: 11/4/2025, 10:05:17 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for j in countS:
            if countS[j] != countT.get(j, 0):
                return False

        return True
        