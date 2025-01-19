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

def longest_repeated_substring(text):
    suffix_array = build_suffix_array(text)
    lcp_array = build_lcp_array(text, suffix_array)

    # Find the maximum LCP and corresponding suffix
    max_length = 0
    index = 0
    for i in range(len(lcp_array)):
        if lcp_array[i] > max_length:
            max_length = lcp_array[i]
            index = suffix_array[i + 1]  # index of the suffix corresponding to this LCP

    # Return the longest repeated substring
    return text[index:index + max_length] if max_length > 0 else ""

# Input handling
def main():
    text = input("Enter the text: ")
    result = longest_repeated_substring(text)
    if result:
        print("Longest repeated substring:", result)
    else:
        print("No repeated substring found.")

# Run the main function
if __name__ == "__main__":
    main()
