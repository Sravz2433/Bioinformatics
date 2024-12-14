def PatternCount(text, pattern):
    count = 0  # Initialize the count to 0
    text_length = len(text)
    pattern_length = len(pattern)
    
    # Loop through all possible starting positions
    for i in range(text_length - pattern_length + 1):
        # Check if the substring matches the pattern
        if text[i:i + pattern_length] == pattern:
            count += 1  # Increment the count if there's a match
    
    return count  # Return the total count

text = 'GCGCG'
pattern ='GCG'
print(PatternCount(text, pattern))  


# Complexity = O(m*n)