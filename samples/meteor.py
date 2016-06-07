# this is a sample file for reading
# in data from a csv using native python
# libraries. note this runs in python 2

import sys

# get filename passed to file
# sys.argv is the list of python
# arguments. Note sys.argv[0] is
# the name of the python program
# i.e. meteor.py
filename = sys.argv[1]

# open file for reading

f = open(filename,"r")

#set up lists to read data to
altitude=[]
energyperkm=[]

linecount=0

#loop over the lines in the file
for line in f:
 
  #ignore header
  if linecount==0:
    header=line
    linecount+=1 
    continue #skips the remainder of the for loop for this line

  linelist=line.split(",") #split the line on comma
  #assign to data lists
  altitude+=[float(linelist[1])] #need to convert to float!
  energyperkm+=[float(linelist[0])]

# close the file
f.close()

# we have the data to work with 
# now lets define some functions

# doubles all the values in a list
def double_elements(ar1):
  #for loops can be written in list definition
  return [element*2.0 for element in ar1]

# integrates the elements of ar1 with respect
# to ar2
def integrates_elements(ar1,ar2):

  # I can only be bothered to 
  # impliment simpsons
  
  n = len(ar1) #length of list
  
  returnlist = []
  for i in range(n): #range generates a list of integer 0 to n-1 
    if i==0:
      returnlist += [(ar1[1]-ar1[0])/ar2[0]]
    elif i==n-1:
      returnlist += [(ar1[n-1]-ar1[n-2])/ar2[n-1]]
    else:
      returnlist += [(ar1[i-1]+4.0*ar1[i]+ar1[i+1])*ar2[i]/6.0]

  # sum up the values in the list
  return sum(returnlist)

# find the energy
energy=integrates_elements(energyperkm,altitude)

print "energy [kt]: " + str(energy) # convert to string

double_energyperkm=double_elements(energyperkm)

# double energy
double_energy=integrates_elements(double_energyperkm,altitude)

print "energy [kt]: " + str(double_energy)

# write new energy to file.

filestring=header

#write each line as a string and append
for i in range(len(altitude)):
  filestring+=str(double_energyperkm[i])+","+str(altitude[i])+"\n"

fout=open("new_meteor.csv","w")
fout.write(filestring)
fout.close()
