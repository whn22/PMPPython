import numpy as np
import pylab as pb


# helper equation
def density_eos(pressure):
  mn=1.0e-30 # setting units arbitarilly
  return ((5.0**(3.0/5.0))*(mn**(8.0/5.0)))/((3**(2.0/5.0))*np.pi**(4.0/5.0))*(pressure**(3.0/5.0))


# function to solve
def TolOppVol(y,radius):

  # mass  
  dm = 4*np.pi*density_eos(y[1])*radius**3
  # pressure
  dP = -(y[1]+density_eos(y[1]))*(y[0] + 4*np.pi*y[1]*radius**3)/(radius*(radius - 2*y[0]))

  return [dm,dP]
 


