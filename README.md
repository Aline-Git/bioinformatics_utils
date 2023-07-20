# bioinformatics_utils
Here are some useful small scripts for bioinformatics

### get_sequence_lengths.py
Given a fasta/q file, returns a table with the readnames (1st column) and their corresponding length (2nd column).

### Prerequisite : 
Biopython needs to be installed 

#### Options : 
-l <min_read_length> will set a minimum threshold on the length

#### Example command line
~/scripts/get_sequence_length.py -l 0 \
  -f ~/raw_data/references/S_aureus/S_aureus_G07I_assembly.fna \
  -t fasta
  
