#!/usr/bin/python
import sys
p = open("o.txt","r")
s = open('s.txt',"w")
lines = p.readlines()
lines.sort()
for line in lines:
	s.write(line)
p.close()
s.close()
