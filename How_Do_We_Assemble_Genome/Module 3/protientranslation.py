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


if __name__ == "__main__":
    # Load codon table from file
    codon_table = load_codon_table('RNA_codon_table_1.txt')
    
    # Example RNA string
    rna_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    
    # Translate RNA to protein
    protein = translate_rna_to_protein(rna_string, codon_table)
    
    print(f"Translated Protein: {protein}")
