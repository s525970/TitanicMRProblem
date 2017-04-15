#opening input file and output files
f = open("titanic.txt","r")  
o = open("moutput.txt", "w") 
for line in f:  
    data = line.strip().split("\t")

#Assigning data into variables if length is a valid value
    #print(len(data))
    if len(data) == 12:
        PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked=data
        print "{0}".format(PassengerId)
        if Survived == "1":
            o.write("{0}\n".format(PassengerId))
#Closing input and output files
f.close()
o.close()
