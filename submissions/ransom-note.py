class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        # Count the number of times each letter occurs in `magazine`
        magazine_counts = {}
        for letter in magazine:
            if letter in magazine_counts:
                magazine_counts[letter] += 1
            else:
                magazine_counts[letter] = 1
        
        # Count the number of times each letter occurs in `ransomNote`
        ransom_note_counts = {}
        for letter in ransomNote:
            if letter in ransom_note_counts:
                ransom_note_counts[letter] += 1
            else:
                ransom_note_counts[letter] = 1
                
            # Ensure each letter in `ransomNote` is not used more than in `magazine`
            if letter not in magazine_counts:
                return False
            if ransom_note_counts[letter] > magazine_counts[letter]:
                return False
    
        return True
