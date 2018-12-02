import random
import numpy
import operator
import pandas as pd
from operator import itemgetter

count_list = []
total_list = []
average_list = []
sorted_list = []
token_list = []
name_counts = []
num_trials = 20

fc = open('gene_overlap_counts_leukemia_Chr1.csv', 'w')
print('Loading overlaps.\n')
with open("Leukemia_Chr1_Overlap.bed", "r") as o:
    overlaps = o.readlines()
    for line in overlaps:
        trial = line.split('\t')[3]
        name = line.split('\t')[7]
        trial_s = trial.split(':')
        name_s = name.split('_')
        name_counts.append((str(trial_s[1]),name_s[0]))

print('Loaded '+str(len(overlaps))+' overlaps.')
    
for r in range(num_trials):
    trial_list = []
    protein_name = []
    protein_counts = []
    print('Running '+str(r+1)+' iteration.\n')
    print ('Loading proteins.\n')
    with open("overlap_counts.txt", "r") as p:
        proteins = p.readlines()
        for line in proteins:
            namep = line.split(' ')[0]
            value = line.split(' ')[1]
            protein_name.append(namep)
    fc.write ('\nRunning '+str(r+1)+' iteration.\n')
    
    print('Getting names and trial counts.')
    print('Processing intersections.\n')
    for trial_total in name_counts:
        if trial_total[0] == str(r+1):
            trial_list.append(trial_total[1])
            total_list.append(trial_total[1])
            protein_name.append(trial_total[1])
    print('success')
    print (len(trial_list))
    print (len(protein_name))

    print('Processing overlap statistics.\n')
    fc.write ('Processing overlap statistics.\n')
    trial_unique, trial_counts = numpy.unique(trial_list, return_counts = True)
    trial_result = list(zip(trial_unique, trial_counts))
    unique, counts =  numpy.unique(total_list, return_counts = True)
    results = dict(zip(unique,counts))
    average_results = dict(zip(unique, counts/num_trials))    
    protein_unique, protein_counts = numpy.unique(protein_name, return_counts = True)
    protein_result = list(zip(protein_unique, protein_counts-1))                            
    c = "\n".join(str(i) for i in protein_result)
    print (c)
    fc.write (c)
    print (trial_result)

average_sorted = sorted(average_results.items(), key=operator.itemgetter(1),reverse=True)
total_sorted = sorted(results.items(), key=operator.itemgetter(1),reverse=True)
average_column_sorted = "\n".join(str(i) for i in average_sorted)
total_column_sorted = "\n".join(str(i) for i in total_sorted)
print ("\nThis is the total number of hits sorted by highest to lowest: \n", total_column_sorted)
fc.write ("\nThis is the total number of hits sorted by highest to lowest: \n" + total_column_sorted)
print ("\nThis is the average number of hits sorted by highest to lowest: \n",average_column_sorted)
fc.write ("\nThis is the average number of hits sorted by highest to lowest: \n" + average_column_sorted)
#print ("\nThis is the total number of hits sorted by highest to lowest: \n", total_sorted)
#print ("\nThis is the average number of hits sorted by highest to lowest: \n", average_sorted)
fc.close()
