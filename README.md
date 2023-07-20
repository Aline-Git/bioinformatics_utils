# bioinformatics_utils
Here are some useful small scripts for bioinformatics

## get_sequence_length.py
Given a fasta/q file, returns a table with the readnames (1st column) and their corresponding length (2nd column).

### Prerequisite : 
Biopython needs to be installed 

### Options : 
-l <min_read_length> will set a minimum threshold on the length

### Example command line
```{bash}
~/scripts/get_sequence_length.py -l 0 \
  -f ~/raw_data/references/S_aureus/S_aureus_G07I_assembly.fna \
  -t fasta
```
## create_fasta_from_seqname_speed_up.py

Given a fasta/q file and a file containing a selection of sequence names to select, the scritp will
search for these sequences in the fasta/q file and put them in a new file. 

If no output filename is given (optional), the new file will be in the same directory as the original 
fasta/q file, with the additional suffix '_selection'.
 
### Options 
-n <names_file> : path to the text file containing the names of the sequences to select, one name per line.
-f <input_fastx> : path to the fasta/q file containing the sequences to fetch (among other).
-t <file_type> : specify the type of fastx input file (fasta or fastq)
-o <output_file> : path to the output file name (optional).

### Prerequisites
This scripts uses a big amount of ram if the input fasta/q is big.
Biopython needs to be installed

### Example command line
```
/home/aline/scripts/create_fasta_from_seqname_speed_up.py \
  -n /mnt/metagenomic/hmmsearch/2010_ppk_in_ref_and_bins/list_of_sequences_to_keep.csv \
  -f /mnt/metagenomic/hmmsearch/2010_ppk_in_ref_and_bins/output_protein_seq_TIGR03705.faa \
  -t fasta
```
