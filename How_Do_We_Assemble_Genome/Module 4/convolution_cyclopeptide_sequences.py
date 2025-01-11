from collections import Counter

def convolution(spectrum):
    """
    Computes the convolution of the given spectrum.
    """
    convolution = []
    for i in range(len(spectrum)):
        for j in range(i + 1, len(spectrum)):
            diff = spectrum[j] - spectrum[i]
            if 57 <= diff <= 200:
                convolution.append(diff)
    return convolution

def top_elements(convolution, M):
    """
    Finds the top M most frequent elements in the convolution (including ties).
    """
    count = Counter(convolution)
    sorted_counts = sorted(count.items(), key=lambda x: (-x[1], x[0]))  # Sort by frequency, then value
    result = []
    for i, (mass, freq) in enumerate(sorted_counts):
        if len(result) < M or freq == sorted_counts[M - 1][1]:  # Include ties
            result.append(mass)
        else:
            break
    return result

def leaderboard_cyclopeptide_sequencing(spectrum, N, amino_acid_masses):
    """
    Implements the Leaderboard Cyclopeptide Sequencing algorithm.
    """
    leaderboard = [""]
    leader_peptide = ""
    parent_mass_value = max(spectrum)
    
    while leaderboard:
        leaderboard = expand_with_masses(leaderboard, amino_acid_masses)
        for peptide in leaderboard[:]:
            if mass(peptide) == parent_mass_value:
                if score(peptide, spectrum) > score(leader_peptide, spectrum):
                    leader_peptide = peptide
            elif mass(peptide) > parent_mass_value:
                leaderboard.remove(peptide)
        
        leaderboard = trim(leaderboard, spectrum, N)
    
    return leader_peptide

def expand_with_masses(peptides, amino_acid_masses):
    """
    Expands peptides by appending each amino acid mass to the current peptides.
    """
    expanded_peptides = []
    for peptide in peptides:
        for mass in amino_acid_masses:
            if peptide:
                expanded_peptides.append(f"{peptide}-{mass}")
            else:
                expanded_peptides.append(f"{mass}")
    return expanded_peptides

def mass(peptide):
    """
    Computes the total mass of a peptide.
    """
    try:
        masses = peptide.split("-")
        print(f"Processing peptide: {peptide}, masses: {masses}")  # Debugging line
        return sum(map(int, masses)) if peptide else 0
    except ValueError as e:
        print(f"Error in mass calculation for peptide '{peptide}': {e}")
        return 0


def cyclospectrum(peptide):
    """
    Computes the cyclic spectrum of a peptide.
    """
    masses = list(map(int, peptide.split("-"))) if peptide else []
    prefix_mass = [0]
    for m in masses:
        prefix_mass.append(prefix_mass[-1] + m)
    peptide_mass = prefix_mass[-1]
    spectrum = [0]
    for i in range(len(masses)):
        for j in range(i + 1, len(masses) + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(masses):
                spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(spectrum)

def score(peptide, spectrum):
    """
    Computes the score of a peptide against the experimental spectrum.
    """
    theoretical = cyclospectrum(peptide)
    spectrum_counter = Counter(spectrum)
    theoretical_counter = Counter(theoretical)
    return sum(min(spectrum_counter[m], theoretical_counter[m]) for m in theoretical_counter)

def trim(leaderboard, spectrum, N):
    """
    Trims the leaderboard to the top N peptides (including ties).
    """
    scored_peptides = [(peptide, score(peptide, spectrum)) for peptide in leaderboard]
    scored_peptides.sort(key=lambda x: -x[1])
    trimmed_leaderboard = []
    for i, (peptide, peptide_score) in enumerate(scored_peptides):
        if len(trimmed_leaderboard) < N or peptide_score == scored_peptides[N - 1][1]:
            trimmed_leaderboard.append(peptide)
        else:
            break
    return trimmed_leaderboard

def convolution_cyclopeptide_sequencing(M, N, spectrum):
    """
    Implements the Convolution Cyclopeptide Sequencing algorithm.
    """
    conv = convolution(spectrum)
    amino_acid_masses = top_elements(conv, M)
    return leaderboard_cyclopeptide_sequencing(spectrum, N, amino_acid_masses)

# Example Usage
if __name__ == "__main__":
    M = 18 # Top M elements from the convolution
    N = 388 # Top N peptides in the leaderboard
    spectrum = [0, 103, 114, 114, 114, 128, 128, 128, 128, 129, 129, 129, 129, 131, 163, 217, 231, 242, 242, 242, 243, 243, 257, 257, 258, 260, 260, 291, 291, 345, 345, 356, 360, 370, 372, 372, 374, 386, 388, 389, 405, 419, 420, 459, 473, 474, 484, 491, 500, 501, 503, 503, 517, 533, 533, 548, 549, 587, 587, 602, 605, 620, 629, 631, 632, 632, 647, 661, 662, 663, 677, 715, 716, 733, 734, 734, 750, 760, 760, 761, 775, 790, 791, 791, 792, 844, 847, 848, 862, 863, 878, 878, 889, 889, 904, 905, 919, 920, 923, 975, 976, 976, 977, 992, 1006, 1007, 1007, 1017, 1033, 1033, 1034, 1051, 1052, 1090, 1104, 1105, 1106, 1120, 1135, 1135, 1136, 1138, 1147, 1162, 1165, 1180, 1180, 1218, 1219, 1234, 1234, 1250, 1264, 1264, 1266, 1267, 1276, 1283, 1293, 1294, 1308, 1347, 1348, 1362, 1378, 1379, 1381, 1393, 1395, 1395, 1397, 1407, 1411, 1422, 1422, 1476, 1476, 1507, 1507, 1509, 1510, 1510, 1524, 1524, 1525, 1525, 1525, 1536, 1550, 1604, 1636, 1638, 1638, 1638, 1638, 1639, 1639, 1639, 1639, 1653, 1653, 1653, 1664, 1767]  # Example spectrum
    
    result = convolution_cyclopeptide_sequencing(M, N, spectrum)
    print("Leader Peptide:", result)
