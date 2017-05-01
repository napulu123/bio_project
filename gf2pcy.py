#! /usr/bin/env python3.5

# this program calculates the nucleotide composition for the features in a genome

# load the system module
import sys



#a function to clean up a DNA sequence
def clean_seq(input_seq):
	#andy += andy
	clean = input_seq.upper()
	clean = clean.replace('N','')	
	return clean
 
def nuc_freq(sequence, base, sig_digs = 2):
	#calculate of the length of sequence
	length = len(sequence)
	

	#count the number of this nucleotide
	count_of_base = sequence.count(base)

	#calculate base frequency
	freq_of_base = count_of_base/length

	#return the frequency and the length
	return( length, round(freq_of_base,sig_digs))

#key = feature_tyoe, value = concatenation of all sequences of that type

#for anything other than calculating AT/GC content

feature_sequences = {}

# declare the file names
gff_file = 'watermelon.gff'
fsa_file = 'watermelon.fsa'

# open the files for reading
gff_in = open(gff_file, 'r')
fsa_in = open(fsa_file, 'r')

# declare variable that will hold the genome sequence
genome = ''

# initialize a line counter
line_number = 0

# read in the genome file
for line in fsa_in:
    # print(str(line_number) + ": " + line)

    # remove newline's - could also use strip
    line = line.rstrip('\n')

    if line_number > 0:
        genome = genome + line

    # increment line_number
    line_number += 1
#add generic function that calculates percentage of a,g,t,c and it has in it 
# did we get the genome correctly?
# print(len(genome))
    
# close the genome file
fsa_in.close()

cds     = ''
trna    = ''
rrna    = ''
intron  = ''
misc    = ''
repeats = ''

# read in the GFF file
for line in gff_in:

    # remove newline's - could also use strip
    line = line.rstrip('\n')

    types = line.split('; type ')
    other_type = types[len(types)-1]
    # print(other_type)
    
    fields = line.split('\t')
    type  = fields[2]
    start = int(fields[3])
    end   = int(fields[4])
    
    # print(type, "\t", start, "\t", end)

    # extract this feature from the genome
    fragment = genome[start-1:end]
    
    fragment = clean_seq(fragment)

    if type in feature_sequences:
    	feature_sequences[type] += fragment	
    else:
	feature_sequences[type] = fragment	
#close gff file
gff_in.close()

for feature,sequence in feature_sequences.items():
	print (feature + '\t' + str(len(sequence))
  # sys.exit()	
	
    if type == 'CDS':
	cds += fragment

    if type == 'intron':
	intron += fragment
    if type == 'misc_feature':
	misc += fragment
    if type == 'repeat_region':
	repeats += fragment

    if type == 'rRNA':
	rrna += fragment
    if type == 'tRNA':
	trna += fragment

#count = -1
#for feature_type in (cds,intron,misc,repeats,trna,rrna):
	#for type in ('cds','intron','misc','repeats','trna','rrna'):	
#loop over the 4 nucleotides
	
	#	for nucleotide in ['A','C','G','T']:
	#		count += 1

#calculate the nucleotidde compodition for each feature
			(feature_length,feature_comp)= nuc_freq(feature_type,base = nucleotide, sig_digs=2)	
					
	#		print(type +'\t' + str(feature_length) + "\t" + str(feature_comp) + nucleotide)
		



# print the output
#print(cds.count('G'))
#print(cds.count('C'))
    

# close the GFF file
gff_in.close()
