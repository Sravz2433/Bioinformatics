def load_codon_table(file_path):
    codon_table = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            codon_table[parts[0]] = parts[1] if len(parts) > 1 else ''
    return codon_table


def translate_rna_to_protein(rna, codon_table):
    peptide = []
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i + 3]
        amino_acid = codon_table.get(codon, '')
        if amino_acid == 'Stop':
            break
        peptide.append(amino_acid)
    return ''.join(peptide)


def dna_to_rna(dna):
    return dna.replace('T', 'U')


def find_peptide_encoding_substrings(dna, peptide, codon_table):
    substrings = []
    rna_length = len(peptide) * 3
    
    for i in range(len(dna) - rna_length + 1):
        substring = dna[i:i + rna_length]
        rna = dna_to_rna(substring)
        translated_peptide = translate_rna_to_protein(rna, codon_table)
        
        if translated_peptide == peptide:
            substrings.append(substring)
    
    return substrings


if __name__ == "__main__":
    # Load codon table from file
    codon_table = load_codon_table('RNA_codon_table_1.txt')
    
    # Example DNA string and peptide
    dna_string = "ATGGCCATGGCGCCCAGAACCTGAGATCAATAGTACCCGTATTAACGGGTGA"
    peptide_string = "MA"
    
    # Find substrings encoding the peptide
    encoding_substrings = find_peptide_encoding_substrings(dna_string, peptide_string, codon_table)
    
    print(f"Encoding Substrings: {encoding_substrings}")
