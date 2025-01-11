def convolution(spectrum):
    # Initialize the list to hold the convolution results
    convolution = []
    
    # Get the length of the spectrum list
    n = len(spectrum)
    
    # Iterate through each pair of elements in the spectrum
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the positive difference
            diff = spectrum[j] - spectrum[i]
            # Add the difference to the convolution list
            convolution.append(diff)
    
    # Return the convolution list with multiplicities considered
    return convolution

# Example usage:
spectrum = [0, 86, 160, 234, 308, 320, 382]
result = sorted(convolution(spectrum))
print(result)
