def shortest_non_shared_substring(text1, text2):
    # Create a set of all substrings of Text2
    substrings_text2 = set()
    len_text2 = len(text2)

    for start in range(len_text2):
        for end in range(start + 1, len_text2 + 1):
            substrings_text2.add(text2[start:end])

    # Now iterate over substrings of Text1 and find the shortest one not in Text2
    len_text1 = len(text1)
    shortest_substring = None

    for start in range(len_text1):
        for end in range(start + 1, len_text1 + 1):
            candidate = text1[start:end]
            if candidate not in substrings_text2:
                # If found, return the first non-shared substring
                if shortest_substring is None or len(candidate) < len(shortest_substring):
                    shortest_substring = candidate
                break  # No need to check longer substrings starting from this index

    return shortest_substring if shortest_substring else ""

# Input handling
def main():
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")
    result = shortest_non_shared_substring(text1, text2)
    if result:
        print("Shortest non-shared substring:", result)
    else:
        print("All substrings of Text1 are shared with Text2.")

# Run the main function
if __name__ == "__main__":
    main()
