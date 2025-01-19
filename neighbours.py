def neighbors(pattern, d):
    """
    Finds the d-neighborhood of a given string pattern.

    Args:
        pattern (str): The input string.
        d (int): The maximum allowed distance (Hamming distance).

    Returns:
        set: A collection of strings (neighbors) within d mismatches from the pattern.
    """
    if d == 0:
        return {pattern}
    if len(pattern) == 0:
        return set()

    nucleotides = ['A', 'C', 'G', 'T']
    first_symbol = pattern[0]
    suffix = pattern[1:]

    # Generate neighbors for the suffix of the pattern
    suffix_neighbors = neighbors(suffix, d)

    result = set()
    for neighbor in suffix_neighbors:
        # If no mismatch, retain the first symbol
        if hamming_distance(suffix, neighbor) < d:
            for nucleotide in nucleotides:
                result.add(nucleotide + neighbor)
        else:
            result.add(first_symbol + neighbor)

    return result

def hamming_distance(s1, s2):
    """
    Calculates the Hamming distance between two strings.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The Hamming distance between s1 and s2.
    """
    return sum(1 for a, b in zip(s1, s2) if a != b)

# Example usage
if __name__ == "__main__":
    pattern = "ACG"
    d = 1
    result = neighbors(pattern, d)
    print("\n".join(result))