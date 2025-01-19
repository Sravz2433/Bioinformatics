class TrieNode:
    def __init__(self):
        self.children = {}
        self.pattern_end = None  # Store the pattern at the end of each pattern path

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pattern, pattern_index):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.pattern_end = pattern_index  # Mark end of a pattern with its index

def prefix_trie_matching(text, trie, start_index, patterns, result):
    node = trie.root
    i = start_index
    while i < len(text):
        char = text[i]
        if char in node.children:
            node = node.children[char]
            if node.pattern_end is not None:
                # We found a match for a pattern
                pattern_index = node.pattern_end
                pattern = patterns[pattern_index]
                result[pattern].append(start_index)
            i += 1
        else:
            break  # No match found
    return

def trie_matching(text, patterns):
    trie = Trie()
    result = {pattern: [] for pattern in patterns}

    # Build the trie from the patterns
    for index, pattern in enumerate(patterns):
        trie.insert(pattern, index)

    # Try to match patterns starting from each position in the text
    for i in range(len(text)):
        prefix_trie_matching(text, trie, i, patterns, result)

    return result

# Input handling
def main():
    text = input("Enter the text: ")
    patterns = input("Enter the space-separated patterns: ").split()

    # Get all positions where patterns match
    pattern_matches = trie_matching(text, patterns)

    # Output result
    for pattern, positions in pattern_matches.items():
        if positions:
            print(f"{pattern}: {' '.join(map(str, positions))}")
        else:
            print(f"{pattern}: No match")

# Run the main function
if __name__ == "__main__":
    main()
