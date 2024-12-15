def Reverse_Complement(Pattern):
    complement={'A':'T','T':'A','C':'G','G':'C'}
    Pattern = Pattern.replace('\n', '')
    reverse_comp = ''.join(complement[base] for base in reversed(Pattern))
    return reverse_comp


text ="AGTC"
print(Reverse_Complement(text))
