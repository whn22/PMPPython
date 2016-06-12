
# example use of raw data
# and try,except and exceptions

# read in user input
usrstr=raw_input("z1: ")
usrstr2=raw_input("z2: ")

# define error class
# not really nessicary
# as this could be replaced
# with a value error
class UserImputError(Exception):
  pass

# helper function
# returns complex number 
# from user input
def usrcomplex_input(input_string):

  # use try/except to raise the 
  # appropriate exception if the
  # user gives an input in the wrong
  # format.

  terms = input_string.split('+') 
  realn=0.0
  imn=0.0

  for trm in terms:
    try:
      if ('j' in trm):
        imn+=float(trm.replace("j", ""))
      elif ('i' in trm):    
        imn+=float(trm.replace("i", ""))
      else:
        realn+=float(trm)
    except:
      raise UserImputError("Could not convert "+input_string+" to a complex")

  return complex(realn,imn)

# convert data to complex
cmpl1 = usrcomplex_input(usrstr)
cmpl2 = usrcomplex_input(usrstr2)

print "= "+str(cmpl1*cmpl2)
