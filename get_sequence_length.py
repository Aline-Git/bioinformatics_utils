#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 Given a fasta file, provide a tab separated table with the names of the sequences on the first column
 and the length of the sequences on the second column. Contigs longeur than <min_len> will be discarded 
 with the option -l <min_len>
 
 It requires that Biopython is installed.
'''

#--------------------------------------------------------------------------------------------------
#                                        Import modules
#--------------------------------------------------------------------------------------------------
#TODO check all these modules are required

from io import StringIO
import os
from os import path
import argparse
import Bio
from Bio import SeqIO


#--------------------------------------------------------------------------------------------------
#                                   Command line examples
#--------------------------------------------------------------------------------------------------

'''
~/scripts/get_sequence_length.py -l 0 \
  -f ~/raw_data/references/S_aureus/S_aureus_G07I_assembly.fna \
  -t fasta
'''

#--------------------------------------------------------------------------------------------------
#                                   Command line parsing
#--------------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description = '')
parser.add_argument('-l', '--minlen', help = 'minimum length for a sequence to be selected', required = True)
parser.add_argument('-f','--fasta', help = 'fasta file with the sequences', required = True)
parser.add_argument('-t','--type', help = 'fasta or fastq', required = True)
parser.add_argument('-o','--output_file', help = 'optional, output file name, if not given, the output filename will constructed from the input file name, same folder.', required = False)

args = parser.parse_args()

minlen = int(args.minlen)
fasta_file_name = args.fasta
file_type = args.type

# if no output filename is given, build one
if args.output_file != None :
    output_file_name = args.output_file
else :
    output_file_name = os.path.splitext(fasta_file_name)[0]+ '_bigger_'+ str(minlen) + '_lengths.tsv'

#--------------------------------------------------------------------------------------------------
#                                   Open files
#--------------------------------------------------------------------------------------------------

fasta_file = open(fasta_file_name,'r')
output_file = open(output_file_name,'w')

#--------------------------------------------------------------------------------------------------
#                               Read and write information
#--------------------------------------------------------------------------------------------------

output_file.write('seqname\tlength\n')

records = list(SeqIO.parse(fasta_file,file_type))
for record in records:
    if len(record.seq) > minlen : 
        output_file.write(record.id + '\t' + str(len(record.seq)) + '\n')

#--------------------------------------------------------------------------------------------------
#                                   Close files
#--------------------------------------------------------------------------------------------------

fasta_file.close()
output_file.close()




