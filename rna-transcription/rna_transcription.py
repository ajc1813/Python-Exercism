def to_rna(dna_strand):
    rna_strand=""
    for nucleotide in dna_strand:
        if nucleotide=="G":
            nucleotide="C"
            rna_strand+=nucleotide
        elif nucleotide=="C":
            nucleotide="G"
            rna_strand+=nucleotide
        elif nucleotide=="T":
            nucleotide="A"
            rna_strand+=nucleotide
        elif nucleotide=="A":
            nucleotide="U"
            rna_strand+=nucleotide
        else:
            return ""
    return rna_strand