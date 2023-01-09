#This here is used to print the header. The Dfam_out_file has a typical error where it tends to
#add a extra fasta_query_name as a second line which is why the program fails
#the next re.find takes care of that

#import re
import sys

sys.stdout=open('C:/Users/khans/Documents/GAVIN/Chris/LTR/LTR_automation/placental_biallelic/out_folder/hits_separated_orgnsmWise/chr_changed_for_annotation/mm10_chr_changed_bed.txt', 'w')

with open('C:/Users/khans/Documents/GAVIN/Chris/LTR/LTR_automation/placental_biallelic/out_folder/hits_separated_orgnsmWise/chr_changed_for_annotation/mm10_chr_changed.txt', 'r') as file:

    for each_line in file:

        each_line=each_line.replace(' ','\t')
        sys.stdout.write(each_line)



