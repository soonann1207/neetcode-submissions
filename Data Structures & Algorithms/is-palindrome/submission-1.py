class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_str = s.lower().replace(" ", "")
        clean_str = "".join(char for char in formatted_str if char.isalnum())
        left, right = 0, len(clean_str)-1
        while left < right:
            if clean_str[left] != clean_str[right]:
                return False
            left += 1
            right -= 1
        
        return True




