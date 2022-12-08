class DNA:
    def __init__(self, seq: str):
        self.seq = seq

    def count(self):
        self.len = len(self.seq)
        print(self.len)

    def transcription(self): #Transcription is the process of producing a strand of RNA from a strand of DNA
        string = ""
        transcription_map = {
            "c": "g",
            "t": "a",
            "a": "u",
            "g": "c",
        }
        
        #Convert DNA--> RNA chain
        for base in self.seq: # For every base for imported DNA is complementary a RNA for transcription
            try:
                string+=transcription_map[base]
            except:
                raise Exception("Error in transcription; base pair not found in transcription map")
                
        return string
        
class RNA:
    def __init__(self, seq: str):
        self.seq = seq
        
    def count(self):
        self.len = len(self.seq)
        print(self.len)
        
    def translation(self):
        amino_acid_sequence = [] #triplet nucleotide called the codon form a single amino acid
        translation_map = {
        "aaa": "Lys",
        "aac": "Asn",
        "aag": "Lys",
        "aau": "Asn",
        "aca": "Thr",
        "acc": "Thr",
        "acg": "Thr",
        "acu": "Thr",
        "aga": "Arg",
        "agc": "Ser",
        "agg": "Arg",
        "agu": "Ser",
        "ucu": "Ser",
        "ucg": "Ser",
        "uca": "Ser",
        "ucc": "Ser",
        "aua": "Ile",
        "auc": "Ile",
        "aug": "Met", #Start Codon
        "auu": "Ile",
        "caa": "Gln",
        "cac": "His",
        "cag": "Gln",
        "cau": "His",
        "cca": "Pro",
        "ccc": "Pro",
        "ccg": "Pro",
        "ccu": "Pro",
        "cga": "Arg",
        "cgc": "Arg",
        "cgg": "Arg",
        "cgu": "Arg",
        "cua": "Leu",
        "cuc": "Leu",
        "cug": "Leu",
        "cuu": "Leu",
        "gaa": "Glu",
        "gac": "Asp",
        "gag": "Glu",
        "gau": "Asp",
        "gca": "Ala",
        "gcc": "Ala",
        "gcg": "Ala",
        "gcu": "Ala",
        "gga": "Gly",
        "ggc": "Gly",
        "ggg": "Gly",
        "ggu": "Gly",
        "gua": "Val",
        "guc": "Val",
        "gug": "Val",
        "guu": "Val",
        "uaa": "STOP",
        "uac": "Tyr",
        "uag": "STOP",
        "uau": "Tyr",
        "uga": "STOP",
        "ugc": "Cys",
        "ugg": "Trp",
        "ugu": "Cys",
        "uuc": "Phe",
        "uug": "Leu",
        "uuu": "Phe",
        "uua": "Leu"
        }
        self.count() # Sets up self.len
        
        if self.len < 3:
            raise Exception("RNA strand is too short for translation. Length should be >= 3 base pairs, and ideally much longer")
        
        start_found = False
        base_pair_counter=0
        # Convert RNA --> protein
        
        for i, base in enumerate(self.seq): #with enumerate gives the acces to item from the iterable
            # If there is not enough RNA left, exit code with amino acid sequence
            if (self.len - i) < 3:
                if amino_acid_sequence == "":
                    raise Exception("No protein found; RNA strand has no start codon before end is reached")
                return amino_acid_sequence
            # If we have not started translation, and a start codon is found, start translation
            elif self.seq[i:i+3] == "aug" and not start_found:
                start_found=True
                amino_acid_sequence.append("Met")
                base_pair_counter+=1
            # If we already found the start codon, every three base pairs, translate the next amino acid
            elif base_pair_counter%3 == 0 and start_found:
                next_codon = self.seq[i:i+3] #check if divisible by 3 and remainder is 0
                try:
                    next_base_pair = translation_map[next_codon]
                except:
                    raise Exception("Next base pair not found because codon does not exist in translation map")
                # If stop codon is encountered, stop translation and return amino acid sequence
                if next_base_pair == "STOP":
                    print(next_codon)
                    return amino_acid_sequence
                else:
                    amino_acid_sequence.append(next_base_pair)
                    base_pair_counter+=1
            # Increment base pair counter when we are not at a codon to keep code running
            elif base_pair_counter%3 != 0 and start_found:
                base_pair_counter+=1
                
        return amino_acid_sequence

    
class Protein:
    def __init__(self,seq:str):
        self.seq = seq
        
    def print_sequence(self):
        print(self.seq)

    def count(self):
        self.len = len(self.seq)
        print(self.len)


def main():
    inputfile = 'dna1.txt'
    f = open(inputfile, "r")
    seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace(" ", "")
    f.close()
    #https://www.ncbi.nlm.nih.gov/nuccore/HQ287898.1
    
    dna_strand = DNA(seq)    
    rna_strand = RNA(dna_strand.transcription())
    protein_sequence = Protein(rna_strand.translation())
    protein_sequence.print_sequence()
    dna_strand.count()
    rna_strand.count()
    protein_sequence.count()
main()
