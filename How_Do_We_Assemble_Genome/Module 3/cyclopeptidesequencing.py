from itertools import permutations

def get_amino_acid_masses():
    """
    Returns a dictionary of amino acids with their respective integer masses.
    """
    return {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
        'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
        'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

def cyclospectrum(peptide):
    """
    Compute the theoretical cyclic spectrum of a peptide.
    """
    prefix_mass = [0]
    peptide_mass = [amino_acid_masses[aa] for aa in peptide]
    n = len(peptide_mass)

    for i in range(n):
        prefix_mass.append(prefix_mass[-1] + peptide_mass[i])

    peptide_mass_total = prefix_mass[-1]
    spectrum = [0]

    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                spectrum.append(peptide_mass_total - (prefix_mass[j] - prefix_mass[i]))

    return sorted(spectrum)

def is_consistent(peptide_spectrum, spectrum):
    """
    Check if the given peptide's linear spectrum is consistent with the provided spectrum.
    """
    spectrum_counts = {mass: spectrum.count(mass) for mass in spectrum}
    peptide_counts = {mass: peptide_spectrum.count(mass) for mass in peptide_spectrum}

    for mass, count in peptide_counts.items():
        if count > spectrum_counts.get(mass, 0):
            return False
    return True

def expand(peptides):
    """
    Expands peptides by appending each amino acid mass to the current peptides.
    """
    expanded_peptides = []
    for peptide in peptides:
        for mass in amino_acid_masses:
            expanded_peptides.append(peptide + mass)
    return expanded_peptides

def parent_mass(spectrum):
    """
    Returns the parent mass of the spectrum, which is the maximum value in the spectrum.
    """
    return max(spectrum)

def mass(peptide):
    """
    Compute the total mass of a peptide.
    """
    return sum(amino_acid_masses[aa] for aa in peptide)

def cyclopeptide_sequencing(spectrum):
    """
    Reconstructs the peptide sequence from the given spectrum.
    """
    candidate_peptides = [""]
    final_peptides = []
    parent_mass_value = parent_mass(spectrum)

    while candidate_peptides:
        candidate_peptides = expand(candidate_peptides)
        for peptide in candidate_peptides[:]:
            if mass(peptide) == parent_mass_value:
                if cyclospectrum(peptide) == spectrum and peptide not in final_peptides:
                    final_peptides.append(peptide)
                candidate_peptides.remove(peptide)
            elif not is_consistent(cyclospectrum(peptide), spectrum):
                candidate_peptides.remove(peptide)

    return final_peptides


if __name__ == "__main__":
    # Example usage
    amino_acid_masses = get_amino_acid_masses()

    spectrum = [0, 113, 128, 186, 241, 299, 314, 427]
    peptides = cyclopeptide_sequencing(spectrum)

    print("Peptides:", peptides)
