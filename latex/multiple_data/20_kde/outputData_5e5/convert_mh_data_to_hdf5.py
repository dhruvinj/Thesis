import h5py
import numpy

rawdata = numpy.loadtxt("testdata.dat")

h5file = h5py.File("chain_data.h5", "w")

h5file.create_dataset("/zoidberg1/data/users/dhruvinj/multiple_data/20_kde/outputData_5e5/E2", data=rawdata[:,0])

h5file.create_dataset("/zoidberg1/data/users/dhruvinj/multiple_data/20_kde/outputData_5e5/E3", data=rawdata[:,1])

