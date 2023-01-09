#!/usr/bin/env/python

#Separating the hits from different species in different files for annotation

import sys

path= 'C:/Users/khans/Documents/GAVIN/Chris/LTR/LTR_automation/placental_biallelic'

sys.stdout= open(path+'/out_folder/hits_separated_orgnsmWise/DAacoCah1.txt', 'w')
with open(path+'/out_folder/placental_biall_Dfamout_hits_colReduced.txt', 'r') as all_LTR_file:
    sys.stdout.write(all_LTR_file.readline())
    for each_line in all_LTR_file:

            #s=each_line.split()

        if each_line.find('DAacoCah1.nrph.hits') != -1:

            sys.stdout.write(each_line)
sys.stdout.close()

sys.stdout= open(path+'/out_folder/hits_separated_orgnsmWise/DAmusPah1.txt', 'w')
with open(path+'/out_folder/placental_biall_Dfamout_hits_colReduced.txt', 'r') as all_LTR_file:
    sys.stdout.write(all_LTR_file.readline())
    for each_line in all_LTR_file:

            #s=each_line.split()

        if each_line.find('DAmusPah1.1.nrph.hits') != -1:
            sys.stdout.write(each_line)
sys.stdout.close()

sys.stdout= open(path+'/out_folder/hits_separated_orgnsmWise/DAmusCar1.txt', 'w')
with open(path+'/out_folder/placental_biall_Dfamout_hits_colReduced.txt', 'r') as all_LTR_file:
    sys.stdout.write(all_LTR_file.readline())
    for each_line in all_LTR_file:

            #s=each_line.split()

        if each_line.find('DAmusCar1.1.nrph.hits') != -1:
            sys.stdout.write(each_line)
sys.stdout.close()

sys.stdout= open(path+'/out_folder/hits_separated_orgnsmWise/DAratNor6.txt', 'w')
with open(path+'/out_folder/placental_biall_Dfamout_hits_colReduced.txt', 'r') as all_LTR_file:
    sys.stdout.write(all_LTR_file.readline())
    for each_line in all_LTR_file:

            #s=each_line.split()

        if each_line.find('DAratNor6.0.nrph.hits') != -1:
            sys.stdout.write(each_line)
sys.stdout.close()

sys.stdout= open(path+'/out_folder/hits_separated_orgnsmWise/DApsaObe2.txt', 'w')
with open(path+'/out_folder/placental_biall_Dfamout_hits_colReduced.txt', 'r') as all_LTR_file:
    sys.stdout.write(all_LTR_file.readline())
    for each_line in all_LTR_file:

        #    s=each_line.split()

        if each_line.find('DApsaObe2.nrph.hits') != -1:
            sys.stdout.write(each_line)
sys.stdout.close()

sys.stdout= open(path+'/out_folder/hits_separated_orgnsmWise/mm10.txt', 'w')
with open(path+'/out_folder/placental_biall_Dfamout_hits_colReduced.txt', 'r') as all_LTR_file:
    sys.stdout.write(all_LTR_file.readline())
    for each_line in all_LTR_file:

#            s=each_line.split()

        if each_line.find('mm10.nrph.hits') != -1:
            sys.stdout.write(each_line)
sys.stdout.close()

sys.stdout= open(path+'/out_folder/hits_separated_orgnsmWise/DAmusSpr1.txt', 'w')
with open(path+'/out_folder/placental_biall_Dfamout_hits_colReduced.txt', 'r') as all_LTR_file:
    sys.stdout.write(all_LTR_file.readline())
    for each_line in all_LTR_file:

 #           s=each_line.split()
        if each_line.find('DAmusSpr1.nrph.hits') != -1:
            sys.stdout.write(each_line)
sys.stdout.close()


sys.stdout= open(path+'/out_folder/hits_separated_orgnsmWise/DAmerUng1.txt', 'w')
with open(path+'/out_folder/placental_biall_Dfamout_hits_colReduced.txt', 'r') as all_LTR_file:
    sys.stdout.write(all_LTR_file.readline())
    for each_line in all_LTR_file:

 #           s=each_line.split()

        if each_line.find('DAmerUng1.nrph.hits') != -1:
            sys.stdout.write(each_line)        
sys.stdout.close()