class Solution:
    def kthCharacter(self, k: int) -> str:
        index = k - 1
        increments = 0
    
        while index > 0:
            p = 1
            while p * 2 <= index:
                p *= 2
            increments += 1
            index -= p
        final_char_code = ord('a') + (increments % 26)
    
        return chr(final_char_code)