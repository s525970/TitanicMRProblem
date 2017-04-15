survivedMaleCount = 0
survivedFemaleCount = 0
malePercentage = 0
femalePercentage = 0
#opening input file and output files
f = open("moutput2.txt","r")
f1 = open("op1.txt","r")
o = open("r2output.txt", "w")
#Each line data will be splitted and stored in data variable 
for line in f:
        
        
        if line.strip() == "male":
                survivedMaleCount+=1
        else:
                survivedFemaleCount+=1
o.write("{0}\t{1}\t{2}\t{3}".format("Survived Male Count:",survivedMaleCount,"Survived Female Count:",survivedFemaleCount))         
for line in f1:
   data = line.strip().split("\t")     
   gender,count = data

   if gender == "female":
        #print((float(survivedMaleCount)/int(count))*100)
        femalePercentage = (float(survivedFemaleCount)/int(count))*100
        print(" femalepercentage",femalePercentage)  
   else:
         malePercentage = (float(survivedMaleCount)/int(count))*100
         print("malePercentage",malePercentage)  
          

   
f.close()
f1.close()
o.close()  
