from Bio import SeqIO

for record in SeqIO.parse('all_matches_to_FUN_020.gbk', 'gb'):
    no_spaces = record.description.replace(' ', '_')
    no_commas = no_spaces.replace(',', '')
    no_brackets = no_commas.replace('(', '')
    no_other_brackets = no_brackets.replace(')', '')
    no_slashes = no_other_brackets.replace('/', '')
    SeqIO.write([record], open(no_slashes + '.gbk', 'w'), 'genbank')

