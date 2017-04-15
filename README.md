# TitanicMRProblem
# MapReduce-Hadoop
Our data set is all about survival details about the passengers in the titanic. The data set consists of passenger’s details of age, gender, ticket fair, passenger’s class and compartment.

We first calculated the total number of males and females, who got survived then their survival percentage.

We created 2 pairs of mapper and reducer class.

# Commands to execute: (local machine)--Running mapper and reducer files individually
execfile('filename')
Example: execfile('mapper.py')
# Data Source:
The data set of our problem is organized and does not need to be cleaned. We chose our data set as there is no solution available on  the internet.
https://github.com/caesar0301/awesome-public-datasets/blob/master/Datasets/titanic.csv.zip (Links to an external site.) (Links to an external site.)
# Steps
1.	We have Titanic.csv file with lot of data
2.	Mapper.py---> Send the data set as a input to the mapper function and we will get output as a key-value pairs, which we will as input to the sort.py ---->
execfile('Mapper.py')
3.	Sort.py-----> Took this mapper output in one file and used it as input to the sort.py and sorted the data in alphabetical order.
execfile('Sort.py')
4.	Reducer.py--> Took sort.py output to one file and pushed this as input to reducer.py file--> Yeah, we got final output as key value pairs and it is required one.
execfile('Reducer.py')
5.	We got final data from the reducer class and used that to visualize it on excel.
# Hadoop Eco System:
Installing Cloudera --> importing Hadoop virtual os ---> writing the commands using Hadoop file system and map reduce will automatically give output

# Map-Reduce Problem01
# Mapper Output
![Mapper 1 Graph](/images/map0.JPG)
# Reducer Output
![redu 1 Graph](/images/redu0.JPG)
# Visual Representation (Total Number of Survivals)
![ 1 Graph](/images/Total.PNG)
# Map-Reduce Problem
# Mapper Output
![Mapper 1 Graph](/images/map2.JPG)
# Reducer Output
![Mapper 1 Graph](/images/redu1.JPG)
# Visual Representation (Number of males and females, who survived) 
![Mapper 1 Graph](/images/Survived.PNG)
# Map-Reduce Problem
# Mapper Output
![Mapper 1 Graph](/images/map3.JPG)
# Reducer Output
![Mapper 1 Graph](/images/redu2.JPG)
# Visual Representation (The final percentage of survival)
![Mapper 1 Graph](/images/Survival.PNG)
# SHARING CODE & SHARING WORK :
Yes, the code can be accessed from a location as our repository is public. Git has been used in pushing the code and I believe, this is the latest form of technology to share your data. Our team performed equally in all the sections. We divided the work and worked on it.
