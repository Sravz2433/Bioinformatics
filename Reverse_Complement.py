def Reverse_Complement(Pattern):
    complement={'A':'T','T':'A','C':'G','G':'C'}
    Pattern = Pattern.replace('\n', '')
    reverse_comp = ''.join(complement[base] for base in reversed(Pattern))
    return reverse_comp

with open('C:/Users/sravy/Downloads/dataset_30273_2 (2).txt','r') as file:
    text = file.read()
    
    
Patternrc=(Reverse_Complement(text))

    
with open('reverse_complement.txt', 'w') as file:
    file.write(Patternrc)

print("Reverse complement has been written to reverse_complement.txt file.")
