import random
import numpy
import operator
import os
from operator import itemgetter

count_list = []
total_list = []
average_list = []
sorted_list = []
token_list = []
iteration_list = ""

num_trials = 20
max_rand_shift = 1000

file = open('leukemia_cosmictrial20.bed', 'w')

print ('Loading variants.\n')
with open ("leukemia_cosmic.bed", "r") as c:
    cosmic = c.readlines()
    for line in cosmic:
        tokens = line.split('\t')
#         chromo = modify[0]
#         start = int(modify[1])
#         end = int(modify[2])
        token_list.append(tokens)
        
        
print ('Loaded ' + str(len(cosmic)) +' variants.')

for r in range(num_trials):
    print ('Running ' + str(r+1) + ' iteration.\n')
    
    trial_list = []
    random.seed()
    ran_pos = int(random.random()*2*max_rand_shift - max_rand_shift)
    randomized = ""
    print ('Shifting and randomizing the regions.')
    
    for modify in token_list:
        
        chromo = modify[0]
        start = int(modify[1])
        end = int(modify[2])
     
        start_s = ran_pos + start
        start_e = ran_pos + end
        
        if start_s > 0:
            randomized = str(chromo) + "\t" + str(start_s) + "\t" + str(start_e) + "\t" + "trial:" + str(r+1) + "\n"
        iteration_list = iteration_list + randomized
        
#print (randomized)
#print (iteration_list)
file.write(iteration_list)
print ("program complete")
file.close()
