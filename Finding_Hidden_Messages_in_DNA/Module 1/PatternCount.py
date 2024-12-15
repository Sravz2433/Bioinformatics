def PatternCount(text, pattern):
    count = 0 
    text_length = len(text)
    pattern_length = len(pattern)
    
    for i in range(text_length - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            count += 1  
            
    return count  

text = 'CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC'
pattern ='CGCG'
print(PatternCount(text, pattern))  

# Complexity = O(m*n)