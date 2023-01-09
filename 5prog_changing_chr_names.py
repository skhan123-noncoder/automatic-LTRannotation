#!/usr/bin/env/python

#Program to change the chromosome number naming (INSDC to number...check NCBI genomes)

import re
import sys

path2='C:/Users/khans/Documents/GAVIN/Chris/LTR/LTR_automation'
path3='/placental_biallelic/out_folder/hits_separated_orgnsmWise/'

with open(path2+'/ncbi_insdc_convert_txt_files/mus_pahari_chr_changes_insdc.txt', 'r') as text_file:

    change_list=[]

    for line in text_file:

        change_list.append((str(line.split()[0]),str(line.split()[1])))

sys.stdout=open(path2+ path3+'/chr_changed_for_annotation/DAmusPah1_chr_changed.txt', 'w')

with open(path2+ path3+ '/DAmusPah1.txt', 'r') as input_file:

    sys.stdout.write(input_file.readline())

    for each_line in input_file:

        for each_entry in change_list:

            if each_entry[1]==str(each_line.split()[0]):

                new_line=re.sub(each_entry[1], each_entry[0], each_line)
                sys.stdout.write(new_line)


#For mus pahari the change list was generated manually
#change_list=[('1','LT608296.1'), ('2','LT608286.1'),('3','LT608290.1'),('4','LT608287.1'),('5','LT608292.1'),
#('6','LT608307.1'),('7','LT608288.1'),('8','LT608301.1'),('9','LT608291.1'),('10','LT608289.1'),('11','LT608304.1'),
#('12','LT608305.1'),('13','LT608299.1'),('14','LT608308.1'),('15,LT608295.1'),('16','LT608294.1'),('17','LT608298.1'),
#('18','LT608302.1'),('19','LT608297.1'),('20','LT608293.1'),('21','LT608306.1'),('22','LT608303.1'),('23','LT608309.1'),
#('X','LT608300.1')]
