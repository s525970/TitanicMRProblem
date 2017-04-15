#!/usr/bin/python

import sys
ip = open("titanic.txt","r")
op1 = open("op1.txt","w")
Total = 0
oldKey = None
lines = ip.readlines()
for line in lines:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, count = data_mapped

    if oldKey and oldKey != thisKey:
        op1.write("{0}\t{1}\n".format(oldKey, Total)) 
        oldKey = thisKey;
        Total = 0

    oldKey = thisKey
    Total += int(count)

if oldKey != None:
   op1.write("{0}\t{1} \n".format(oldKey, Total)) 
op1.close()









