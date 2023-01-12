#A set in which each key-value pair indicates a codon and its corresponding protein is first defined
#From the test cases, it is seen that the each codon is obtained by taking three consecutive letters of the strap starting from the right. So a list of codons is obtained from the strand using the wrap() function
#Now iteration is done over the lements of the codon list and value corresponding to each codon is obtained from the codon-protein set
#The protein value is added to an empty list if it is not 'STOP' otherwise the loop is broken and the list of codons is returned
import textwrap #Imports the textwrap module
def proteins(strand):
    codon_protein={'AUG':'Methionine',
             'UUU':'Phenylalanine',
             'UUC':'Phenylalanine',
             'UUA':'Leucine',
             'UUG':'Leucine',
             'UCU':'Serine',
             'UCC':'Serine',
             'UCA':'Serine',
             'UCG':'Serine',
             'UAU':'Tyrosine',
             'UAC':'Tyrosine',
             'UGU':'Cysteine',
             'UGC':'Cysteine',
             'UGG':'Tryptophan',
             'UAA':'STOP',
             'UAG':'STOP',
             'UGA':'STOP'
            } #Creates a set in which each key-value pair represents a codon and its corresponding protein
    codon_list=textwrap.wrap(strand, 3) #Converts the strand into a list in which each element is formed by three consecutive elements of the strand
    protein=[] #Creates an empty list
    for codon in codon_list: #Iterates over the codons in the list of codons
        protein_value=codon_protein[codon] #Obtains the protein corresponding to a codon from the set of codon and protein 
        if protein_value=='STOP': #Checks whether the protein is 'STOP'
            break #Breaks the loop
        else:
            protein.append(protein_value) #Adds the protein to the empty list
    return protein #returns the proteins
        

    
    








