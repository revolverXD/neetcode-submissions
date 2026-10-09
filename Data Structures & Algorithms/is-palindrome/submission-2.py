import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = string.ascii_lowercase + string.digits
        s = s.lower().strip()
        new_string = ""
        for c in s:
            if c in alphaNum:
                new_string += c
        if new_string == new_string[::-1]:
            return True
        return False


        