from collections import Counter

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        # Calculate score for each word
        word_scores = []
        for word in words:
            word_score = sum(score[ord(char) - ord('a')] for char in word)
            word_scores.append(word_score)
        
        # Count available letters
        letter_count = Counter(letters)
        
        # Helper function to check if a word can be formed with available letters
        def can_form_word(word, available):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > available[char]:
                    return False
            return True
        
        # Helper function to use backtracking to find maximum score
        def backtrack(index, available, current_score):
            if index == len(words):
                return current_score
            
            # Skip the current word
            max_score = backtrack(index + 1, available, current_score)
            
            # Include the current word if possible
            word = words[index]
            if can_form_word(word, available):
                # Use the letters in the current word
                word_count = Counter(word)
                for char in word_count:
                    available[char] -= word_count[char]
                # Calculate the score including the current word
                max_score = max(max_score, backtrack(index + 1, available, current_score + word_scores[index]))
                # Backtrack: restore the letters
                for char in word_count:
                    available[char] += word_count[char]
            
            return max_score
        
        # Start backtracking from the first word
        return backtrack(0, letter_count, 0)
    
words =["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score= [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

print(maxScoreWord( words, letters, score))