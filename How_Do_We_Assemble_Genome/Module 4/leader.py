from collections import Counter

amino_acid_mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101,
    'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156,
    'Y': 163, 'W': 186
}

def cyclic_spectrum(peptide):
    prefix_mass = [0]
    for mass in peptide:
        prefix_mass.append(prefix_mass[-1] + mass)
    peptide_mass = prefix_mass[-1]
    cyclic_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                cyclic_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(cyclic_spectrum)

def score(peptide, spectrum):
    peptide_spectrum = cyclic_spectrum(peptide)
    spectrum_counter = Counter(spectrum)
    peptide_counter = Counter(peptide_spectrum)
    score = 0
    for mass in peptide_counter:
        score += min(peptide_counter[mass], spectrum_counter[mass])
    return score

def trim(leaderboard, spectrum, N):
    if len(leaderboard) <= N:
        return leaderboard
    scores = [(peptide, score(peptide, spectrum)) for peptide in leaderboard]
    scores.sort(key=lambda x: x[1], reverse=True)
    cutoff_score = scores[N-1][1]
    return [peptide for peptide, sc in scores if sc >= cutoff_score]

def leaderboard_cyclopeptide_sequencing(spectrum, N):
    amino_acids = list(amino_acid_mass.values())
    leaderboard = [[]]
    leader_peptide = []
    parent_mass = max(spectrum)
    
    while leaderboard:
        leaderboard = [peptide + [aa] for peptide in leaderboard for aa in amino_acids]
        new_leaderboard = []
        for peptide in leaderboard:
            if sum(peptide) == parent_mass:
                if score(peptide, spectrum) > score(leader_peptide, spectrum):
                    leader_peptide = peptide
            elif sum(peptide) < parent_mass:
                new_leaderboard.append(peptide)
        leaderboard = trim(new_leaderboard, spectrum, N)
    
    return leader_peptide

# Example usage:
N = 115
spectrum = [0, 97, 97, 99, 101, 101, 103, 103, 113, 113, 114, 114, 115, 115, 128, 128, 129, 131, 137, 137, 147, 147, 163, 186, 186, 194, 202, 204, 214, 216, 217, 226, 227, 228, 230, 234, 242, 251, 256, 260, 262, 264, 265, 278, 287, 294, 301, 316, 317, 317, 323, 323, 327, 327, 330, 331, 331, 333, 333, 348, 370, 374, 379, 393, 393, 395, 424, 429, 430, 430, 430, 431, 432, 434, 438, 441, 445, 446, 446, 448, 450, 451, 460, 476, 477, 507, 507, 527, 531, 533, 542, 543, 544, 544, 547, 556, 560, 561, 561, 566, 573, 574, 576, 579, 579, 581, 585, 597, 604, 634, 640, 644, 647, 657, 657, 658, 660, 661, 663, 664, 675, 691, 693, 694, 701, 702, 710, 713, 716, 728, 728, 741, 742, 748, 755, 757, 760, 762, 763, 764, 777, 778, 803, 804, 808, 824, 830, 830, 838, 841, 841, 843, 843, 844, 854, 860, 861, 863, 875, 877, 877, 879, 891, 892, 906, 907, 927, 927, 931, 945, 955, 955, 957, 967, 972, 974, 978, 980, 988, 990, 990, 990, 991, 1006, 1007, 1008, 1019, 1024, 1026, 1029, 1034, 1042, 1058, 1068, 1071, 1086, 1087, 1091, 1092, 1093, 1094, 1102, 1103, 1105, 1108, 1134, 1135, 1137, 1139, 1141, 1147, 1153, 1157, 1166, 1171, 1176, 1184, 1189, 1194, 1194, 1205, 1208, 1208, 1217, 1223, 1233, 1234, 1236, 1249, 1254, 1254, 1262, 1268, 1272, 1284, 1286, 1289, 1294, 1295, 1304, 1313, 1320, 1320, 1321, 1322, 1323, 1331, 1336, 1350, 1357, 1357, 1361, 1369, 1385, 1386, 1399, 1403, 1415, 1417, 1419, 1419, 1420, 1422, 1424, 1426, 1435, 1441, 1450, 1458, 1464, 1468, 1470, 1472, 1483, 1487, 1488, 1498, 1506, 1516, 1517, 1521, 1532, 1534, 1536, 1540, 1546, 1554, 1563, 1569, 1578, 1580, 1582, 1584, 1585, 1585, 1587, 1589, 1601, 1605, 1618, 1619, 1635, 1643, 1647, 1647, 1654, 1668, 1673, 1681, 1682, 1683, 1684, 1684, 1691, 1700, 1709, 1710, 1715, 1718, 1720, 1732, 1736, 1742, 1750, 1750, 1755, 1768, 1770, 1771, 1781, 1787, 1796, 1796, 1799, 1810, 1810, 1815, 1820, 1828, 1833, 1838, 1847, 1851, 1857, 1863, 1865, 1867, 1869, 1870, 1896, 1899, 1901, 1902, 1910, 1911, 1912, 1913, 1917, 1918, 1933, 1936, 1946, 1962, 1970, 1975, 1978, 1980, 1985, 1996, 1997, 1998, 2013, 2014, 2014, 2014, 2016, 2024, 2026, 2030, 2032, 2037, 2047, 2049, 2049, 2059, 2073, 2077, 2077, 2097, 2098, 2112, 2113, 2125, 2127, 2127, 2129, 2141, 2143, 2144, 2150, 2160, 2161, 2161, 2163, 2163, 2166, 2174, 2174, 2180, 2196, 2200, 2201, 2226, 2227, 2240, 2241, 2242, 2244, 2247, 2249, 2256, 2262, 2263, 2276, 2276, 2288, 2291, 2294, 2302, 2303, 2310, 2311, 2313, 2329, 2340, 2341, 2343, 2344, 2346, 2347, 2347, 2357, 2360, 2364, 2370, 2400, 2407, 2419, 2423, 2425, 2425, 2430, 2431, 2438, 2443, 2443, 2444, 2448, 2457, 2460, 2460, 2461, 2462, 2471, 2473, 2477, 2497, 2497, 2527, 2528, 2544, 2553, 2554, 2556, 2558, 2558, 2559, 2563, 2566, 2570, 2572, 2573, 2574, 2574, 2574, 2575, 2580, 2609, 2611, 2611, 2625, 2630, 2634, 2656, 2671, 2671, 2673, 2673, 2674, 2677, 2677, 2681, 2681, 2687, 2687, 2688, 2703, 2710, 2717, 2726, 2739, 2740, 2742, 2744, 2748, 2753, 2762, 2770, 2774, 2776, 2777, 2778, 2787, 2788, 2790, 2800, 2802, 2810, 2818, 2818, 2841, 2857, 2857, 2867, 2867, 2873, 2875, 2876, 2876, 2889, 2889, 2890, 2890, 2891, 2891, 2901, 2901, 2903, 2903, 2905, 2907, 2907, 3004]

result = leaderboard_cyclopeptide_sequencing(spectrum, N)
# Convert the result list of integers to the required output format:
result_str = '-'.join(map(str, result))
print(result_str)
