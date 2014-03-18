

class CodonTable(object):
    """Defines how to make a codon table.
    """

    def __init__(self, source_file):
        print 'boom'

        # e.g.{'AAA': 'T', 'AAG': 'R'}
        self.codon_to_amino_acid_map = {}

        # Key to list
        # e.g.{'T': ['AAA', 'CCC', 'GGG'], 'A': ['CGC']}
        self.amino_acid_to_codon_map

    def translate_codon(self, codon):
        """Return amino acid corresponding to codon.
        """
        return self.codon_to_amino_acid_map[codon]

    def reverse_translate_amino_acid(self, amino_acid):
        codon_options = self.amino_acid_to_codon_map[amino_acid]

        # Somehow make a choice.  For now, just first one.
        codon = codon_options[0]

        # Return the one we chose.
        return codon


if __name__ == '__main__':
    my_codon_table = CodonTable('standard_usage.txt')
    print my_codon_table.translate_codon('AAA')
    print my_codon_table.reverse_translate_amino_acid('F')

    my_second_codon_table = CodonTable('weird_usage.txt')
