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
import numpy as np
from scipy.stats import gaussian_kde,skew,skewtest,kurtosis
import h5py

tick_label_fontsize=18
axis_label_fontsize=18
matplotlib.rc('xtick', labelsize=tick_label_fontsize )
matplotlib.rc(('xtick.major','xtick.minor'),  pad=10)
matplotlib.rc('ytick', labelsize=tick_label_fontsize)

chain_data_file = h5py.File('chain_data.h5', 'r')

print "Reading Data"
E2 = chain_data_file['/zoidberg1/data/users/dhruvinj/multiple_data/flamespeed_calculation/E2']
E3 = chain_data_file['/zoidberg1/data/users/dhruvinj/multiple_data/flamespeed_calculation/E3']

E2_sub_data = E2[100000:4000000:20]
E3_sub_data = E3[100000:4000000:20]

print "Reading Model Data"
model_output = np.loadtxt("modelpoints.dat")
print "Done Readng Model Data"

fig1 = plot.figure()
ax1 = fig1.add_subplot(111)

ax1.hist( model_output[:,0], bins=250, align='mid')
ax1.plot( (0.182, 0.182), (0, 160000), 'r-')
ax1.errorbar( 0.182, 80000, xerr=0.15*0.182, ecolor='red')
ax1.set_xlabel( r"$V_f$", fontsize=axis_label_fontsize)
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0) )
fig1.savefig("flame_20.pdf", bbox_inches='tight')

print "Done with Figure 1"

fig2 = plot.figure()
ax2 = fig2.add_subplot(111)

ax2.hist( model_output[:,1], bins=250, align='mid')
ax2.plot( (0.522, 0.522), (0, 160000), 'r-')
ax2.errorbar( 0.522, 80000, xerr=0.15*0.522, ecolor='red')
ax2.set_xlabel( r"$V_f$", fontsize=axis_label_fontsize)
ax2.ticklabel_format(style='sci', axis='x', scilimits=(0,0) )
fig2.savefig("flame_28.pdf", bbox_inches='tight')

print "Done with Figure 2"

fig3 = plot.figure()
ax3 = fig3.add_subplot(111)

ax3.hist( model_output[:,2], bins=250, align='mid')
ax3.plot( (1.25, 1.25), (0, 180000), 'r-')
ax3.errorbar(1.25, 90000, xerr=1.25*0.15, ecolor='red')
ax3.set_xlabel( r"$V_f$", fontsize=axis_label_fontsize)
ax3.ticklabel_format(style='sci', axis='x', scilimits=(0,0) )
fig3.savefig("flame_40.pdf", bbox_inches='tight')

print "Done with Figure 3"

fig4 = plot.figure()
ax4 = fig4.add_subplot(111)

ax4.hist( model_output[:,3], bins=250, align='mid')
ax4.plot( (1.66, 1.66), (0, 180000), 'r-')
ax4.errorbar( 1.66, 90000, xerr=0.15*1.66, ecolor='red')
ax4.set_xlabel( r"$V_f$", fontsize=axis_label_fontsize)
ax4.ticklabel_format(style='sci', axis='x', scilimits=(0,0) )
fig4.savefig("flame_46.pdf", bbox_inches='tight')

print "Done with Figure 4"

fig5 = plot.figure()
ax5 = fig5.add_subplot(111)

ax5.hist( model_output[:,4], bins=250, align='mid')
ax5.plot( (2.1, 2.1), (0, 160000), 'r-')
ax5.errorbar( 2.1, 80000, xerr=0.15*2.1, ecolor='red')
ax5.set_xlabel( r"$V_f$", fontsize=axis_label_fontsize)
ax5.ticklabel_format(style='sci', axis='x', scilimits=(0,0) )
fig5.savefig("flame_53.pdf", bbox_inches='tight')

print "Done with Figure 5"

fig6 = plot.figure()
ax6 = fig6.add_subplot(111)

ax6.hist( model_output[:,5], bins=250, align='mid')
ax6.plot( (3.31, 3.31), (0, 160000), 'r-')
ax6.errorbar( 3.31, 80000, xerr=0.15*3.31, ecolor='red')
ax6.set_xlabel( r"$V_f$", fontsize=axis_label_fontsize)
ax6.ticklabel_format(style='sci', axis='x', scilimits=(0,0) )
fig6.savefig("flame_75.pdf", bbox_inches='tight')

print "Done with Figure 6"

fig7 = plot.figure()
ax7 = fig7.add_subplot(111)

ax7.hist( model_output[:,6], bins=250, align='mid')
ax7.plot( (4.75, 4.75), (0, 160000), 'r-')
ax7.errorbar( 4.75, 80000, xerr=0.15*4.75, ecolor='red')
ax7.set_xlabel( r"$V_f$", fontsize=axis_label_fontsize)
ax7.ticklabel_format(style='sci', axis='x', scilimits=(0,0) )
fig7.savefig("flame_100.pdf", bbox_inches='tight')

print "Done with Figure 7"

plot.show()
