import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                print(s[i], s[j])
                return False
            i += 1
            j -= 1
        return True