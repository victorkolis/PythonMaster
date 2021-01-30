#!/usr/bin/env python3

def DNA_strand(dna):
	DNA = {'A': 'T',
	'T': 'A',
	'G': 'C',
	'C': 'G'}
	complementary_dna= ''
	for nucleobases in dna:
		complementary_dna += DNA[nucleobases]
	return complementary_dna
	
print(DNA_strand("A"))
