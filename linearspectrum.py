from collections import Counter

def get_amino_acid_mass():
    return {
        'G': 57,   # Glycine
        'A': 71,   # Alanine
        'S': 87,   # Serine
        'P': 97,   # Proline
        'V': 99,   # Valine
        'T': 101,  # Threonine
        'C': 103,  # Cysteine
        'I': 113,  # Isoleucine
        'L': 113,  # Leucine
        'N': 114,  # Asparagine
        'D': 115,  # Aspartic Acid
        'Q': 128,  # Glutamine
        'K': 128,  # Lysine
        'E': 129,  # Glutamic Acid
        'M': 131,  # Methionine
        'H': 137,  # Histidine
        'F': 147,  # Phenylalanine
        'R': 156,  # Arginine
        'Y': 163,  # Tyrosine
        'W': 186   # Tryptophan
    }

def LinearSpectrum(Peptide):
    # Get the amino acid masses
    mass_table = get_amino_acid_mass()
    
    # Initialize the PrefixMass array with 0 at the first position
    PrefixMass = [0] * (len(Peptide) + 1)
    
    # Fill in the PrefixMass array
    for i in range(1, len(Peptide) + 1):
        amino_acid = Peptide[i - 1]
        PrefixMass[i] = PrefixMass[i - 1] + mass_table[amino_acid]

    # Initialize the LinearSpectrum with 0
    LinearSpectrum = [0]
    
    # Compute all subpeptide masses
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
    
    # Return the sorted LinearSpectrum
    print(sorted(LinearSpectrum))
    return sorted(LinearSpectrum)

def score_peptide(peptide, spectrum):
    """Calculate the score of a peptide against a given spectrum."""
    linear_spectrum = LinearSpectrum(peptide)
    spectrum_counter = Counter(spectrum)
    linear_spectrum_counter = Counter(linear_spectrum)
    
    score = 0
    for mass in linear_spectrum_counter:
        score += min(linear_spectrum_counter[mass], spectrum_counter[mass])
    
    return score

# Example usage
# peptide = "VYYEVDWTMGRQIDPDEYPIAQCTRHRATILTLPDWQM"
# print(LinearSpectrum(peptide))
peptide = "PEEP"
spectrum = [0, 97, 97, 129, 194, 196, 226, 226, 244, 258, 323, 323, 452]

score = score_peptide(peptide, spectrum)

print(f"The score of peptide {peptide} against the given spectrum is: {score}")