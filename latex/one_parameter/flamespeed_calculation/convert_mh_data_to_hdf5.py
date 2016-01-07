import h5py
import numpy

rawdata = numpy.loadtxt("testdata.dat")

h5file = h5py.File("chain_data.h5", "w")

h5file.create_dataset("/zoidberg1/data/users/dhruvinj/one_parameter/flamespeed_calculation/E3", data=rawdata[:])


