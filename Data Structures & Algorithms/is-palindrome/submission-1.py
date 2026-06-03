class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = ""
        for ch in s:
            if ch.isalnum():
                arr += ch.lower()
        if arr == arr[::-1]:
            return True
        else:
            return False
            