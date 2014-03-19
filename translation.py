from collections import defaultdict
#import the Sequence class definition     (note: the name of the class is "Seq") 
from Bio.Seq import Seq 
from Bio.Seq import translate #not Translate!!!!!! 
#import the IUPAC alphbet definitions 
from Bio.Alphabet import generic_dna, generic_protein, IUPAC 
from Bio.Data import CodonTable 
  
class CodonTable(object):
    """Defines how to make a codon table.
    """

    def __init__(self, source_file):
        #print 'boom'

        # e.g.{'AAA': 'T', 'AAG': 'R'}
        self.codon_to_amino_acid_map = {}
        CUTinput = open('ecoli-codon-usage.txt')
        for line in CUTinput:
        parts = line.split()
        #print parts
        a = 0
           while a < len(parts):
        #print parts[a]
        #print parts[a+1]
        codon = parts[a]
        AA = parts[a+1]
        self.codon_to_amino_acid_map[codon] = AA
        a = a+5
        
        # Key to list
        #iterate through codon_to_amino_acid_map to find each instance of an amino acid and add the corresponding codon to this new list.  inverse(codon_to_amino_acid_map)...
        # e.g.{'T': ['AAA', 'CCC', 'GGG'], 'A': ['CGC']}
        self.amino_acid_to_codon_map = defaultdict(list) #if the value is going to show up mutliple time in TUCinput, then using defaultdict(set)
        TUCinput = open('ecoli-codon-usage.txt')
        for line in TUCinput:
            parts2 = line.split()
            b = 0
            while b < len(parts2):
                codon = parts2[b]
                AA = parts2[b+1]
                self.amino_acid_to_codon_map[AA].append(codon) #if using defaultdict(set), then change append(codon) to add(codon)
                b = b+5

        self.amino_acid_to_weight_map = defaultdict(list)
        Freqinput = open('ecoli-codon-usage.txt')
        for line in Freqinput:
            parts = line.split()
            a = 0
            while a < len(parts):
                AA = parts[a+1]
                Freq = parts[a+2]
                self.amino_acid_to_weight_map[AA].append(Freq)
                a = a+5

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
    #print my_codon_table.codon_to_amino_acid_map#['AAA']
    #print len(my_codon_table.codon_to_amino_acid_map)
    #print my_codon_table.amino_acid_to_codon_map
    #print len(my_codon_table.amino_acid_to_codon_map)
    #print my_codon_table.amino_acid_to_codon_map['A']
    #print my_codon_table.amino_acid_to_weight_map
    #print my_codon_table.translate_codon('AAA')
    #print my_codon_table.reverse_translate_amino_acid('F')

    #my_second_codon_table = CodonTable('weird_usage.txt')

    #create a Sequence object and assign it to TolC 
TolC = Seq("MKKLLPILIGLSLSGFSSLSQAENLMQVYQQARLSNPELRKSAADRDAAFEKINEARSPL" + \
        "LPQLGLGADYTYSNGYRDANGINSNATSASLQLTQSIFDMSKWRALTLQEKAAGIQDVTY" + \
        "QTDQQTLILNTATAYFNVLNAIDVLSYTQAQKEAIYRQLDQTTQRFNVGLVAITDVQNAR" + \
        "AQYDTVLANEVTARNNLDNAVEQLRQITGNYYPELAALNVENFKTDKPQPVNALLKEAEK" + \
        "RNLSLLQARLSQDLAREQIRQAQDGHLPTLDLTASTGISDTSYSGSKTRGAAGTQYDDSN" + \
        "MGQNKVGLSFSLPIYQGGMVNSQVKQAQYNFVGASEQLESAHRSVVQTVRSSFNNINASI" + \
        "SSINAYKQAVVSAQSSLDAMEAGYSVGTRTIVDVLDATTTLYNAKQELANARYNYLINQL" + \
        "NIKSALGTLNEQDLLALNNALSKPVSTNPENVAPQTPEQNAIADGYAPDSPAPVVQQTSA" + \
        "RTTTSNGHNPFRN*", IUPAC.protein) 

for line in TolC:
    #print line
    tolC = []



#TolCstr = TolCstr.split
#print TolCstr
  
#tolC = TolC.back_translate[1]#(table='Standard') 
#tolC = back_translate(TolC, table='Standard', stop_symbol='*', to_stop=True, cds=True) 
#tolC = standard_translator.back_translate(TolC) 
#print tolC 
  
#output = open('20140318revtrans.txt','w') 
#output.write(tolC + '\n') 
#output.close()
