#!/usr/bin/env python3.5

#load the system module
import sys

#declare the file names
gff_file =' watermelon.gff'
fsa_file =' watermelon.fsa'

#open the file for reading

gff_in = open(gff_file,'r')
fsa_in= open(fsa_file,'r')

#declare variable to hold genome
genome = ''

#initialize a line counter
line_number = 0

#read in genome file
for line in fsa_file:
        #print(str(line_number) + ':' + line)
	#remove newline's- could also use strip
    line = line.rstrip('\n')
    if line_number > 0:
		genome = genome + line
	#increment line_number
    line_number += 1

#did we get the genome correctly?
print(len(genome))

#close file
fsa_in.close()

for line in gff_file:
	fields = line.split('\t')
	type = fields[2]	
	start = fields[3]
	end = fields[4]
	print (type,'\t',start, '\t', end)
