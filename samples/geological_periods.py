import sys

# example of dictionary usage

period = sys.argv[1]

# set up dictionary
period_dict={}

# add data
period_dict['Cambrian']=(541.0,485.4)
period_dict['Ordovician']=(485.4,443.4)
period_dict['Silurian']=(443.4,419.2)
period_dict['Devonian']=(419.2,358.9)
period_dict['Carboniferous']=(358.9,298.9)
period_dict['Permian']=(298.9,252.2)
period_dict['Triassic']=(252.2,201.3)
period_dict['Jurassic']=(201.3,145.0)
period_dict['Cretaceous']=(145.5,66.0)
period_dict['Paleogene']=(66.0,23.0)
period_dict['Neogene']=(23.0,2.6)
period_dict['Ternary']=(66.0,2.6)
period_dict['Quaternary']=(2.6,0.0)

# look up data
print period
print 'duration: ' + str(period_dict[period][0] - period_dict[period][1])
