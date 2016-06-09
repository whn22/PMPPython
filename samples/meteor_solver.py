import numpy as np
import sys
from scipy.integrate import odeint
import pylab as pb

filename=sys.argv[1]

data=np.loadtxt(filename,skiprows=1,delimiter=",")


# helper functions
def iso_density(z):
  return 1.4*np.exp(-z/8000.0)

# y = [v,L,Ldif,z]

# define the equations to solve
def meteor_equations(y,t, mass,density):

  Cd=2.0
  
  dv = - (Cd*iso_density(y[3])*(y[1]*y[0])**2)/mass 
  dL = y[2]
  dLdif = Cd*iso_density(y[3])*(y[0]**2)/(y[1]*density)
  dz = -y[0]

  return [dv,dL,dLdif,dz]

# set up initial data

v=20000.0 # velocity
L=100.0 # diameter
Ldif=0.0 # d diameter/dt 
z=60000.0 # altitude
rho=3000.0 # density

y0 = [v,L,Ldif,z]

#parameter
mass=(1.0/6.0)*rho*np.pi*L**3

# values of dependent variable
# to evaluate at
times=np.linspace(0.0,4.0)

solution_ar = odeint(meteor_equations,y0,times,args=(mass,rho))

# compute energy (mass*v^2/2) derivative wrt
# to altitude to compare with data
energy = 0.5*mass*(solution_ar[:,0])**2

#compute gradient
denerdz = np.gradient(energy)/np.gradient(solution_ar[:,3])

# plot data
pb.plot(data[:,0],data[:,1])

kt=1.0/2.39e-13

#plot model - need to have consistent units
pb.plot(1000.0*denerdz/kt,solution_ar[:,3]/1000.0)

pb.show()






