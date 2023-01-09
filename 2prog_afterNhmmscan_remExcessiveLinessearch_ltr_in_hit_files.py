#!/usr/bin/env/python

#Program to search for the LTR output file in final hit list and output the result to a new file

import glob
#import string
import sys
import re

path= '/bi/home/khans/Gavin_Kelsey/Chris_Belton/project_LTR/LTR_annotation_folder'
input_file_name='/placental_biallelic/placental_biallelic_dfamtblout'
output_file_name='/placental_biallelic/out_folder/placental_biallelic_dfamout_hits.txt'
temp_file_name='/placental_biallelic/placental_biallelic_dfamtblout_tempfile.txt'

sys.stdout=open(path+temp_file_name, 'w')

with open(path+input_file_name, 'r') as ltr_out_file:
    
    line1= ltr_out_file.readlines()
    
    for each in line1:
        
        if not re.search('#', each):
            each2=re.sub(r'\s+', '\t', each)
            sys.stdout.write(each2)
            sys.stdout.write('\n')
            
sys.stdout.close()

ltr_out_file.close()

def main():
    temp_file1= return_searchlist()
    final_out= search()

def return_searchlist():
    search_list=[]
    
    with open (path+input_file_name, 'r') as input_file:
        
        for line in input_file:
            
            if not re.search('#', line):
                
                temp=(line.split()[0], line.split()[2])
                search_list.append(temp)
    
    input_file.close()    
    
    return(search_list)
    
def search():
    
    sys.stdout=open(path+output_file_name, 'w')
    
    query_list=return_searchlist()
    
    with open(path+'/hit_files_used_for_LTR_search/header.txt', 'r') as header_file:
        
        header=header_file.readline()
        header=re.sub(r'\n', '\t', header)
        header=[str(header), 'fasta_query_name']
        
    print('\t'.join(header))
    header_file.close()
    

    for each in query_list:
        for each_file in glob.glob(path+'/hit_files_used_for_LTR_search/*.hits'):
            
            with open(each_file, 'r') as search_file:
                
                for each_line in search_file:
                    
                    if each_line.find(str(each[0])) != -1:
                        
                        each_line=re.sub(r'\n', '\t', each_line)
                        list_out_with_label=[str(each_line), str(each[1]), '\n']
        sys.stdout.write('\t'.join(list_out_with_label))
sys.stdout.close()
    
if __name__=='__main__':
    main()
