def approximate_pattern_matching(pattern, text, d):

    positions = []

   

    for i in range(len(text) - len(pattern) + 1):

        window = text[i:i+len(pattern)]

        mismatches = sum(c1 != c2 for c1, c2 in zip(pattern, window))

       

        if mismatches <= d:

            positions.append(i)

   

    return positions

 
pattern = "CCAATCCAC"
with open("C:/Users/sravy/Downloads/dataset_30278_4 (2).txt", 'r') as file:
    text = file.read()
    
d = 6


result = approximate_pattern_matching(pattern, text, d)

result_str = ' '.join(map(str, result))
print(result_str)