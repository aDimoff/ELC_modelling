## this code plots RV data and folded RV data against the best fit model from ELC.
## inputs : folder name of system modeled by ELC
## outputs: plots of RV data

import numpy as np
import matplotlib.pyplot as plt
import sys, getopt
from argparse import ArgumentParser

# reset defalult plotting values
plt.rcParams['figure.figsize'] = (14, 7)
plt.rc('font', family='sans-serif')
plt.rc('axes', labelsize=14)
plt.rc('axes', labelweight='bold')
plt.rc('axes', titlesize=16)
plt.rc('axes', titleweight='bold')
plt.rc('axes', linewidth=2)
plt.rc('xtick',labelsize=14,direction='in',top=True)
plt.rc('ytick',labelsize=14,direction='in',right=True)

print('\n','input system =',(sys.argv)[1])

## read input directory name from command line
input_directory = (sys.argv)[1]
input_RVs_file = (sys.argv)[2]
input_RVs_file = str(input_directory)+'/'+str(input_RVs_file)
input_fold_file = str(input_directory)+'/ELCdataRV1.fold'
input_model_file = str(input_directory)+'/star1.RV'
input_model_del_file = str(input_directory)+'/star1.delRV'

Names = ['time','RV','RV_err']
RV_in = np.genfromtxt(input_RVs_file,names=Names,unpack=False)
Names = ['model_time','model_RV']
model_in = np.genfromtxt(input_model_file,names=Names,unpack=False)
Names = ['fold_time','fold_RV','fold_err']
fold_in = np.genfromtxt(input_fold_file,names=Names,unpack=False)

plt.figure(figsize=(8,8))
plt.errorbar(RV_in['time'],RV_in['RV'],yerr=RV_in['RV_err'],marker='.',ls='',capsize=4,color='red')
plt.grid()
#plt.show()
plt.savefig(str(input_directory)+'RV_full.png',rasterize=True,bbox_inches=None,dpi=300)

plt.figure(figsize=(8,8))
plt.plot(model_in['model_time'],model_in['model_RV'],ls='-',lw=1.5,color='black')
plt.errorbar(fold_in['fold_time'],fold_in['fold_RV'],fold_in['fold_err'],marker='.',ls='',capsize=4,color='red')
plt.errorbar(fold_in['fold_time']+1,fold_in['fold_RV'],fold_in['fold_err'],marker='.',ls='',capsize=4,color='red')
plt.xlim(0,2)
plt.grid()
#plt.show()
plt.savefig(str(input_directory)+'RV_model.png',rasterize=True,bbox_inches=None,dpi=300)

print('\n','End of Line')