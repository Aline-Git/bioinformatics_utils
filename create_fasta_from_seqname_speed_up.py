#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Given a fasta/q file and a file containing a selection of sequence names to select, the scritp will
search for these sequences in the fasta/q file and put them in a new file. 

If no output filename is given (optional), the new file will be in the same directory as the original 
fasta/q file, with the additional suffix '_selection'.

This scripts uses a big amount of ram if the input fasta/q is big.
'''

#--------------------------------------------------------------------------------------------------
#                                        Import modules
#--------------------------------------------------------------------------------------------------

from io import StringIO
import os
from os import path
import argparse
import Bio
from Bio import SeqIO
import time

print('Biopython v',Bio.__version__)
#--------------------------------------------------------------------------------------------------
#                                   Command line example
#--------------------------------------------------------------------------------------------------

'''
~/home/aline/scripts/create_fasta_from_seqname_speed_up_test.py \
  -n /mnt/metagenomic/hmmsearch/2010_ppk_in_ref_and_bins/list_of_sequences_to_keep.csv \
  -f /mnt/metagenomic/hmmsearch/2010_ppk_in_ref_and_bins/output_protein_seq_TIGR03705.faa \
  -o output_file_name
  -t fasta
'''


#--------------------------------------------------------------------------------------------------
#                                   Parsing command line
#--------------------------------------------------------------------------------------------------


parser = argparse.ArgumentParser(description = 'Script for selection of sequences from fasta or fastq by name')
parser.add_argument('-n', '--namefile', help = 'file with the name of the wanted sequences, one name per line', required = True)
parser.add_argument('-f','--fastx', help = 'fasta/q file with the sequences', required = True)
parser.add_argument('-o','--output_filename', help = 'output filename (optional)', required = False)
parser.add_argument('-t','--type', help = 'fasta or fastq', required = True)

args = parser.parse_args()

namefile_name = args.namefile
fastx_file_name = args.fastx

if args.output_filename != None :
    output_file_name = args.output_filename
else :
    output_file_name = os.path.splitext(fastx_file_name)[0]+ '_selection.' + args.type

fastx_file_name = args.fastx
index_filename =  os.path.splitext(fastx_file_name)[0]+ '.idx' 

file_type = args.type


#**************************************** Program *************************************************

#--------------------------------------------------------------------------------------------------
#                                       0. Open files
#--------------------------------------------------------------------------------------------------


namefile = open(namefile_name,'r')

fastx_file = open(fastx_file_name,'r')
output_file = open(output_file_name,'w')

#--------------------------------------------------------------------------------------------------
#                                       1. Initialization
#--------------------------------------------------------------------------------------------------


seqname_list = []
seqname_list_trouve = []
seqname = ''

#--------------------------------------------------------------------------------------------------
#                                     2. Read sequence names
#--------------------------------------------------------------------------------------------------

print('collecting the names of the sequence to copy\n')
# go through the file containing the names of the sequences we want to keep
line = namefile.readline()
while line :
    seqname = line.split('\t')[0].replace('\n','')
    #print seqname

    # make a list of the sequence names we want to keep
    if seqname not in seqname_list :
        seqname_list.append(str(seqname))
    line = namefile.readline()

namefile.close()

#--------------------------------------------------------------------------------------------------
#                                    3. Select sequences
#--------------------------------------------------------------------------------------------------
print('fetching the sequences in file ', fastx_file_name)

start_time = time.process_time()
compte = 0
indexed_file = SeqIO.index(fastx_file_name,file_type)

# go through the list of sequences that we want to copy
for seqname in seqname_list :
    
    # if the sequence is in the indexed file : 
    try : 
        output_file.write(indexed_file[seqname].format(file_type))
        compte += 1
        seqname_list_trouve.append(seqname)
        
    except :
        print(seqname, 'was not found')

fastx_file.close()
output_file.close()

end_time = time.process_time()

print('*** script complete ***')
print('CPU search time : ', end_time - start_time)# in fractional seconds
print('number of sequences looked for : ',len(seqname_list))
print('numer of sequences found :',compte)







