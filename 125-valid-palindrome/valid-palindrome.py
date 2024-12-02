class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for x in s:
            if x.isalnum():
                new += x.lower()
        p1, p2 = 0, len(new)
        while p1 < p2:
            if new[p1] != new[p2 -1]:
                return False
            p1 += 1
            p2 -= 1
        return True
               