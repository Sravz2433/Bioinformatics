def build_suffix_array(text):
    suffixes = sorted((text[i:], i) for i in range(len(text)))
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def build_lcp_array(text, suffix_array):
    n = len(text)
    rank = [0] * n
    lcp = [0] * (n - 1)

    # Create rank array
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i

    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while (i + h < n and j + h < n and text[i + h] == text[j + h]):
                h += 1
            lcp[rank[i] - 1] = h  # Length of LCP for the pair (i, j)
            if h > 0:
                h -= 1  # Decrease h for the next suffix comparison
    return lcp

def longest_shared_substring(text1, text2):
    # Concatenate the two texts with a unique delimiter
    combined_text = text1 + '#' + text2 + '$'
    
    suffix_array = build_suffix_array(combined_text)
    lcp_array = build_lcp_array(combined_text, suffix_array)

    max_length = 0
    start_index = 0

    # Check the LCP array for the longest shared substring
    for i in range(1, len(lcp_array)):
        # Check if the suffixes come from different parts (one from text1 and one from text2)
        if (suffix_array[i] < len(text1) and suffix_array[i - 1] > len(text1)) or \
           (suffix_array[i] > len(text1) and suffix_array[i - 1] < len(text1)):
            if lcp_array[i - 1] > max_length:
                max_length = lcp_array[i - 1]
                start_index = suffix_array[i]

    # Return the longest shared substring
    return combined_text[start_index:start_index + max_length] if max_length > 0 else ""

# Input handling
def main():
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")
    result = longest_shared_substring(text1, text2)
    if result:
        print("Longest shared substring:", result)
    else:
        print("No shared substring found.")

# Run the main function
if __name__ == "__main__":
    main()
