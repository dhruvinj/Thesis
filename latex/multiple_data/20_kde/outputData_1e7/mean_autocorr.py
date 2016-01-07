#!/usr/bin/python

import sys
import os
import glob

from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from matplotlib import rc

matplotlib.rcParams['path.simplify'] = True
rc('text',usetex=True)

# Different modes
# By default, you can "show()" the figure which gives you an interactive window
# and it will save a .png when you call savefig().
# PDF produces a .pdf file, but show() doesn't seem to work.
#matplotlib.use("PDF")

import matplotlib.pyplot as plot
import numpy as np
from scipy.stats import gaussian_kde
import h5py

# Column 0: gamma_CN
# Column 1: gamma_N
# Column 2: T_a
h5_file = h5py.File('chain_data.h5', 'r')

print "Reading Data"
E2_data = h5_file['/zoidberg1/data/users/dhruvinj/multiple_data/20_kde/outputData_1e7/E2']
E3_data= h5_file['/zoidberg1/data/users/dhruvinj/multiple_data/20_kde/outputData_1e7/E3']

E3_sub_data=E3_data[0:10000000]
E2_sub_data=E2_data[0:10000000]


tick_label_fontsize=18
axis_label_fontsize=18
matplotlib.rc('xtick', labelsize=tick_label_fontsize )
matplotlib.rc(('xtick.major','xtick.minor'),  pad=10)
matplotlib.rc('ytick', labelsize=tick_label_fontsize)

E2_mean = np.zeros(E2_sub_data.size)
E3_mean = np.zeros(E3_sub_data.size)

for i in xrange(E2_sub_data.size):
    E2_mean[i] = np.mean(E2_sub_data[0:i])
    E3_mean[i] = np.mean(E3_sub_data[0:i])

fig = plot.figure()
ax1 = fig.add_subplot(111)

gn = ax1.set_xlabel( "Sample Number", fontsize=axis_label_fontsize)
gcn = ax1.set_ylabel( "Average", fontsize=axis_label_fontsize)

ax1.plot(E2_mean,linestyle='-',color='blue',lw=2,label=" E2 ")
ax1.plot(E3_mean,linestyle='-',color='red',lw=2,label= " E3 ")

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels)

ax1.grid(True)

fig.savefig("M1_running_avg.pdf", bbox_inches='tight')

#Autocorrelation
E3_sub_data=E3_data[10000:10000000]
E2_sub_data=E2_data[10000:10000000]

fig2 = plot.figure()
ax2 = fig2.add_subplot(111)

ax2.set_xlabel( "Sample Number", fontsize=axis_label_fontsize)
ax2.set_ylabel( "Autocorrelation", fontsize=axis_label_fontsize)

gcn = ax2.acorr(E3_sub_data-np.mean(E3_data), usevlines=False, maxlags=None, normed=True, lw=2, linestyle='-', marker='.',color='red', label= " E3 ")
gn = ax2.acorr(E2_sub_data-np.mean(E2_data), usevlines=False, maxlags=None, normed=True, lw=2, linestyle='-', marker='.', color='blue',label= " E2 ")

ax2.set_xbound(lower=0, upper=50)

handles2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(handles2, labels2)

ax2.grid(True)

fig2.savefig("M1_autocorr.pdf", bbox_inches='tight')


