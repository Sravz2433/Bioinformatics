def hamming_distance(str1, str2):
    # Ensure both strings have equal length
    if len(str1) != len(str2):
        raise ValueError("Input strings must have equal length")

    # Initialize distance counter
    distance = 0
    
    # Iterate through the characters of the strings and count differences
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1
    
    return distance

# Read both strings from the file
with open('c:/Users/sravy/Downloads/dataset_30278_3.txt', 'r') as file:
    string1 = file.readline().strip()
    string2 = file.readline().strip()

# Calculate the Hamming distance and print the result
print("Hamming distance:", hamming_distance(string1, string2))
