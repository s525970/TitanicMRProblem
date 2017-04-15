

survivedCount = 0
#opening input file and output files
f = open("moutput.txt","r")  
o = open("r1output.txt", "w")
#Each line data will be splitted and stored in data variable 
for line in f:
        survivedCount+=1
o.write("{0}\t{1}".format("Survived Count:",survivedCount))         
f.close()
o.close()  
