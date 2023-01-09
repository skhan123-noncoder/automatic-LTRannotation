#!/usr/bin/env/python

#Program to combine the columns and arrange in a different file

#import re
#import string
#import sys
import re
#import os
#import glob
#import pandas as pd
import sys

path= 'C:/Users/khans/Documents/GAVIN/Chris/LTR/LTR_automation/placental_biallelic'

def main():
    short=shorten()

def shorten():

    #for each in glob.glob(path+'/output_files/*'):
    
        #filename=os.path.basename(each)
    sys.stdout= open(path+'/out_folder/placental_biall_Dfamout_hits_colReduced.txt', 'w')

    with open (path+'/out_folder/placental_biallelic_dfamout_hits.txt', 'r') as each_file:

#This here is used to print the header. The Dfam_out_file has a typical error where it tends to
#add a extra fasta_query_name as a second line which is why the program fails
#the next re.search within the for loop takes care of that

        header=each_file.readline()
        h=header.split()
        h.append(str(h[1])+'__'+str(h[2])+'__'+str(h[15])+'__'+str(h[-1]))
        print(h[0],h[9],h[10],h[-1],h[4],h[8])

        for each_line in each_file:

            if not re.search('fasta_query_name', each_line):

                s=each_line.split()
                #print(s)
                s.append(str(s[1])+'__'+str(s[2])+'__'+str(s[15])+'__'+str(s[-1]))
                print(s[0],s[9],s[10],s[-1],s[4],s[8])
    sys.stdout.close()
                      

if __name__=='__main__':
    main()