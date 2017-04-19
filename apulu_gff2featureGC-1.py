
!/usr/bin/env python3.5

# this script reads  and parse the GC content

#load the system module
import sys

#set the name of the input file
file = 'watermelon.fsa'
#open the file
infile = open(file,'r')
sequence = infile.read()
infile.close()
line_number = 0
for line in sequence:
	line = line.strip('\n')
	if line_number > 0:
		del line_number [0:14] #SLicing off FASTA header
	line_number += 1
sequence = ''.join(sequence)
total_bp = sequence.count('A') + sequence.count('T') + sequence.count('G') + sequence.count('C')

total_GC = sequence.count + sequence.count('C')
GC_content = (float(total_GC) / float(total_bp)) * 100
print (GC_content)

#Possible loop
#d = { 'G':0, 'C':0, 'A':0, 'T':0 }
#count = 0
#for line in infile
#	if count == 0
#		count += 1
#		continue
#	d[line] += 1

