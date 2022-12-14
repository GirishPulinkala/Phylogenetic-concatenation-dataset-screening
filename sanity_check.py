import sys

def check_double_seqs(fastaname):
    identifiers = []
    matches=[]
    with open(fastaname, "r") as fh:
        for line in fh:
            if line.startswith(">"):
                seq_id = line[1:-1]
                if seq_id not in identifiers:
                    identifiers.append(line[1:-1])
                elif seq_id in identifiers:
                  print( "not empty!")
                  break
                  
                    
                
input_fasta=sys.argv[1]      
check_double_seqs(input_fasta)