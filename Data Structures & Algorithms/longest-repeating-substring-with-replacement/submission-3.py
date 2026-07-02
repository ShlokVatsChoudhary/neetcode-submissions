class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        max_freq = 0
        left = 0
        
        for right, char in enumerate(s):
            # Map 'A'-'Z' to index 0-25
            idx = ord(char) - 65  
            counts[idx] += 1
            
            # Keep track of the historical maximum frequency in any valid window
            max_freq = max(max_freq, counts[idx])

            # If the window requires more than k replacements, shift it forward
            if (right - left + 1) - max_freq > k:
                counts[ord(s[left]) - 65] -= 1
                left += 1
                
        return len(s) - left
