dna_to_rna = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def to_rna(sequence):
    mapped = map(lambda x: dna_to_rna[x], list(sequence))
    return ''.join(mapped)
