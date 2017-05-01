#!/usr/bin/env python3.5

#function to clean up a DNA sequence

def clean_seq(input_seq):
	clean = input_seq.upper()
	clean = clean.replace('N',")
	return clean
#function to clean up a DNA sequence

def nuc_count(sequence,base_1,base_2):
	length=len(sequence)
	base_1_count = sequence.count(base_1)
	base_2_count = sequence.count(base_2)
	combined_base_count = base_1_count + base_2_count
	base_freq =(combined_base_count/length) * 100
	percent = round(raw_percent, 2)
	

	return_percent
#function to write complemtary strand

def comp(seq):
	comp = (seq.replace('A','t'))
	
	comp = (seq.replace('C','g'))
	
	comp = (seq.replace('T','a'))
	
	comp = (seq.replace('G','c'))
	
	return comp.upper()


#function for gene name

def exon_name(gff_line):
	break_1 = line.split('Gene')
	break_2 = break_1[1].split(';')
	exon = break_2[0].strip()

	print (exon)
	return exon
	
#Make dictionary
#key = feature_type, value = concatenation of all sequence of that type 

feature sequences = {}
#key = exon, value = sequences
exon_sequences = {}
#key = gene, value = all exons in that gene
gene_sequences ={}

import sys
import collections

if len(sys.argv) <3:
	print(sys.argv[0] +":requires.fasta and .gff files")
	sys.exit()


fsa = sys.argv[1]
gff = sys.argv[2]

fsa_file = open(watermelon.fsa,'r')
genome= ''

for line in fsa_file:
	if not line.starts with ('>')"
		genome = genome + line.strip()
fsa_file.close()

genome_length = len(genome)


gff_file = open(watermelon.gff,'r')

for line in gff_file:
	stuff = line.split('	')
	feature = stuff[2].strip()
	start_index = int(stuff[3]) -1
	strand = clean_seq(genome[start_index: int(stuff[4])])
	
	if feature in feature_sequences:
		feature_sequences[feature] = feature_sequences[feature] + stranf
	else:
		feature_sequences[feature] = strand

	stuff = line.split('t')
	if data[2].strip() == 'CDS'
		exon = exon_name(line)
		start_index = int(stuff[3]) -1
		strand = clean_seq(genome [start_index:int(stuff[4])])
		
		if stuff[6].strip() == '-':
			complement_strand= comp(strand)
			exon_sequnces[exon] = complement_strand
		else:	
			exon_sequences[exon] = strand
gff_file.close()

ordered_exons = collections.OrderedDict(sorted(exon_sequences.items()))

for exon,sequence in ordered_exon.items():
	split_exon = exon.split('')
	if '-' in split_exon[0]:
		split_exon = split_exon[0].split('-')
	if split_exon[0] in gene_sequences:
		gene_sequences[split_exon[0]] += sequence
	else:
		gene_sequences[split_exon[0]] = sequence


for feature_type,sequence in feature_sequences.items():
	GC_percent = nuc_count(sequence, 'C','G')
	feature_percent = (len(sequence)/genome_length) * 100
	formated_feature_percent = '(' + str(roun(fature_percent,1)) + '%)'
	template = "{0:15}{1:7}{2:7}{3:25}"
	
	print(template.format(feature_type,len(sequence), formated_feature_percent,GC_percent))


for gene,sequence in gene_sequences.items():
	print('>' + gene)
	print( sequence + '\n')




#fxn for reverse complement
#fxn for G + C
#print/store/cuild CDS for each gene
#capture gene name




