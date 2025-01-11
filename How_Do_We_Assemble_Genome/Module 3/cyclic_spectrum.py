# Dictionary of amino acid masses (using integer masses for simplicity)
amino_acid_mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101,
    'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156,
    'Y': 163, 'W': 186
}

def peptide_to_mass(peptide):
    """Convert a peptide sequence to its mass."""
    return sum(amino_acid_mass[aa] for aa in peptide)

def generate_cyclic_spectrum(peptide):
    """Generate the cyclic spectrum of a given peptide sequence."""
    n = len(peptide)
    extended_peptide = peptide + peptide  # Simulate cyclic nature
    cyclic_spectrum = [0]

    # Generate all subpeptides and calculate their masses
    for length in range(1, n):
        for start in range(n):
            subpeptide = extended_peptide[start:start + length]
            mass = peptide_to_mass(subpeptide)
            cyclic_spectrum.append(mass)

    cyclic_spectrum.append(peptide_to_mass(peptide))  # Include the mass of the entire peptide
    cyclic_spectrum = sorted(cyclic_spectrum)
    return cyclic_spectrum

# Example usage
peptide = "VYYEVDWTMGRQIDPDEYPIAQCTRHRATILTLPDWQM"
cyclic_spectrum = generate_cyclic_spectrum(peptide)

# Write the cyclic spectrum to a file as a list
output_file = 'cyclic_spectrum.txt'
with open(output_file, 'w') as file:
    file.write(str(cyclic_spectrum))

print(f"Cyclic spectrum of peptide {peptide} has been written to {output_file} as a list")
