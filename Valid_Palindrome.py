# Blind 75: Valid Palindrome on Leetcode
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases
# Solution 1
class Solution1:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        newstr = ''

        for c in s:
            if c.isalnum():
                newstr += c.lower()
        return newstr == newstr[::-1]  # reverse string


# Solution 2


class Solution2:
    def isPalindrome(t: str) -> bool:
        l, r = 0, len(t) - 1
        while l <= r:
            while not t[l].alNumDetect():
                l += 1
            while not t[r].alNumDetect():
                r -= 1
            if t[l].lower == t[r].lower:
                return False
        return True

    def alNumDetect(p):
        return ord('A') <= ord(p) <= ord('Z') or ord('a') <= ord(p) <= ord('z') or ord('0') <= ord(p) <= ord('9')
        # ord function get the ascii code
