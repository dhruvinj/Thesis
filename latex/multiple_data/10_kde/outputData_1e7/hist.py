#!/usr/bin/python
import sys
import os
import glob
import matplotlib
from matplotlib import rc
rc('text',usetex=True)

# Different modes
# By default, you can "show()" the figure which gives you an interactive window
# and it will save a .png when you call savefig().
# PDF produces a .pdf file, but show() doesn't seem to work.
#matplotlib.use("PDF")

import matplotlib.pyplot as plot
from numpy import *
from scipy.stats import gaussian_kde,skew,skewtest,kurtosis
import h5py

h5_file = h5py.File('chain_data.h5', 'r')

print "Reading Data"
E2_data = h5_file['/zoidberg1/data/users/dhruvinj/multiple_data/10_kde/outputData_1e7/E2']
E3_data= h5_file['/zoidberg1/data/users/dhruvinj/multiple_data/10_kde/outputData_1e7/E3']

E3_sub_data = E3_data[10000:10000000:20]
E2_sub_data = E2_data[10000:10000000:20]

print "Computing stats"
E3_mean = mean(E3_sub_data)
E3_sigma = std(E3_sub_data)

E2_mean =  mean(E2_sub_data)
E2_sigma = std(E2_sub_data)

print "E2 stats:"
print "Mean: ", E2_mean
print "Std. Dev.: ", E2_sigma
print "Skewness: ", skew(E2_sub_data)
print "Kurtosis: ", kurtosis(E2_sub_data)
print " "

print "E3 stats:"
print "Mean: ", E3_mean
print "Std. Dev.: ", E3_sigma
print "Skewness: ", skew(E3_sub_data)
print "Kurtosis: ", kurtosis(E3_sub_data)
print " "

def gaussian(mu,sigma,x):
    return 1.0/(sigma*sqrt(2*pi))*exp(-0.5*((x-mu)/sigma)**2);


tick_label_fontsize=18
axis_label_fontsize=18
matplotlib.rc('xtick', labelsize=tick_label_fontsize )
matplotlib.rc(('xtick.major','xtick.minor'),  pad=10)
matplotlib.rc('ytick', labelsize=tick_label_fontsize)

fig = plot.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel( " E3 ", fontsize=axis_label_fontsize)
ax1.set_ylabel( "Output Samples", fontsize=axis_label_fontsize)

print "Plotting Histogram"
ax1.hist( E3_sub_data, bins=250, align='mid' )

ax2 = ax1.twinx()

print "Computing KDE"
density = gaussian_kde(E3_data)

x = linspace(-10, 70, 5000)

print "Plotting KDE"
#ax2.plot( x, density(x), 'k--', linewidth=1 )
ax2.plot(x, gaussian(E3_mean,E3_sigma,x), 'r-', linewidth=1 )

ax2.set_xbound(lower=-10, upper=70)
ax2.set_ylabel( "PDF", fontsize=axis_label_fontsize)
#ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0) )
#ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0) )

ax1.grid(True)

print "Saving Figure"
plot.savefig("E3.pdf", bbox_inches='tight')

############################################
# Average N
############################################

fig2 = plot.figure()
ax3 = fig2.add_subplot(111)
ax3.set_xlabel( " E2 ", fontsize=axis_label_fontsize)
ax3.set_ylabel( "Output Samples", fontsize=axis_label_fontsize)

print "Plotting Histogram"
ax3.hist( E2_sub_data, bins=250, align='mid' )

ax4 = ax3.twinx()

#print "Computing KDE"
#density = gaussian_kde(E3_data)

x = linspace(-10.0, 70, 5000)

print "Plotting KDE"
#ax2.plot( x, density(x), 'k--', linewidth=1 )
ax4.plot(x, gaussian(E2_mean,E2_sigma,x), 'r-', linewidth=1 )

ax4.set_xbound(lower=-10, upper=70)
ax4.set_ylabel( "PDF", fontsize=axis_label_fontsize)
ax3.grid(True)

print "Saving Figure"
plot.savefig("E2.pdf", bbox_inches='tight')


