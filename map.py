#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv

f = open('titanic.csv')
o = open('o.txt',"w")
csv_f=csv.reader(f)

for line in csv_f:
    sex = line[4]
    o.write("{0}\t{1}\n".format(sex, "1"))
o.close()

