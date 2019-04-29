#!/usr/bin/python

import os
import sys
import pdb

import re

import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np

import pickle

def main():
  print("In main analysis")
  run_dir = "/home/vishal/UMassD/sem2/astro_phy/project/runs"
  os.chdir(run_dir)
  cmd = 'find shock_* -iname LOGS_part5'
  results = os.popen(cmd).read().split('\n')
  #print(results)
  count = 1
  masses = []
  Zs = []
  all_data = []
  fe_core_z1 = [] # z=0.0001
  fe_core_z2 = [] # z=0.001
  fe_core_z3 = [] # z=0.01
  fe_core_z4 = [] # z=0.1
  
  si_core_z1 = [] # z=0.0001
  si_core_z2 = [] # z=0.001
  si_core_z3 = [] # z=0.01
  si_core_z4 = [] # z=0.1

  initial_mass_z1 = []
  initial_mass_z2 = []
  initial_mass_z3 = []
  initial_mass_z4 = []

  final_rem_masses = []
  corrs_mass = []
  tot_ran = 0
  G = 6.67408e-11
  M_sol = 1.98e+30
  for paths in results:
    if paths == "":
      continue
    print(paths)
    count += 1
    #pdb.set_trace()
    model_name = paths.split('/')[1]
    mass = float(re.findall('M_[0-9.]+',model_name)[0].split('_')[-1])# this is a string
    masses.append(mass)
    print("mass:"+str(mass))
    z = float(re.findall('Z_[0-9.]+',model_name)[0].split('_')[-1])# this is a string
    print("z:"+str(z))
    Zs.append(z)
    # read the history.data file and extract the Fe, Si mass.
    
    #LOG_name = 'LOGS_finish/'
    #data_path = paths.split('/')[-3] + "/" + paths.split('/')[-2]
    # us the data_path
    #pdb.set_trace()
    try:
      l = mr.MesaLogDir(paths)
      pl = l.profile_data()
    except:
      print("Not able to read data from " + paths)
      continue
    M_in = pl.data('mass') * M_sol
    R_in = pl.data('radius_cm') * 10**-2
    vel_esc_sq = 2 * G * (M_in/R_in)

    vel_sq = (pl.data('vel_km_per_s') * 10**3)**2

    a = vel_sq[-200:-1] < vel_esc_sq[-200:-1]
    try:
      mass_indx = np.where(a==True)[0][0]
    except:
      print("issues")
      continue
    rem_mass = pl.data('mass')[-200:-1][mass_indx] # solar masses
    tot_ran += 1
    final_rem_masses.append(rem_mass)
    corrs_mass.append(mass)

    """
    #d = mr.MesaData(data_path + "/LOGS_finish/history.data")
    fe_core_mass = d.data('fe_core_mass')[-1]
    si_core_mass = d.data('si_core_mass')[-1]
    all_data.append((mass,z,fe_core_mass,si_core_mass))
    #pdb.set_trace()
    if (z == 0.0001):
      fe_core_z1.append(fe_core_mass)
      si_core_z1.append(si_core_mass)
      initial_mass_z1.append(mass)
    elif (z==0.001):
      fe_core_z2.append(fe_core_mass)
      si_core_z2.append(si_core_mass)
      initial_mass_z2.append(mass)
    elif (z == 0.01):
      fe_core_z3.append(fe_core_mass)
      si_core_z3.append(si_core_mass)
      initial_mass_z3.append(mass)
    elif (z==0.1):
      fe_core_z4.append(fe_core_mass)
      si_core_z4.append(si_core_mass)
      initial_mass_z4.append(mass)
    """
  pdb.set_trace()

########################################################################
# Plot for Fe core and Si shell mass after the ms_to_ccsn models
  pdb.set_trace()
  # Plot the results:
  plt.figure(1)
  plt.subplot(2,2,1)
  plt.scatter(initial_mass_z1,fe_core_z1,marker='^')
  plt.scatter(initial_mass_z1,si_core_z1,marker='s')
  #plt.scatter(initial_mass_z1,np.log10(fe_core_z1))
  plt.title('z=0.0001')
  #plt.xlabel('Initial Progenitor($M_\odot\$)')
  plt.ylabel('Core Mass($M_{\odot}$)')

  plt.subplot(2,2,2)
  plt.scatter(initial_mass_z2,fe_core_z2,marker='^')
  plt.scatter(initial_mass_z2,si_core_z2,marker='s')
  #plt.scatter(initial_mass_z2,np.log10(fe_core_z2))
  plt.title('z=0.001')
  #plt.xlabel('Initial Progenitor($M_\odot\$)')
  #plt.ylabel('Fe Core($M_\odot\$)')

  plt.subplot(2,2,3)
  plt.scatter(initial_mass_z3,fe_core_z3,marker='^')
  plt.scatter(initial_mass_z3,si_core_z3,marker='s')
  #plt.scatter(initial_mass_z3,np.log10(fe_core_z3))
  plt.title('z=0.01')
  plt.xlabel('Main Sequence Mass($M_{\odot}$)')
  plt.ylabel('Core Mass($M_{\odot}$)')

  plt.subplot(2,2,4)
  plt.scatter(initial_mass_z4,fe_core_z4,marker='^')
  plt.scatter(initial_mass_z4,si_core_z4,marker='s')
  #plt.scatter(initial_mass_z4,np.log10(fe_core_z4))
  plt.title('z=0.1')
  plt.xlabel('Main Sequence Mass($M_{\odot}$)')
  #plt.ylabel('Fe Core($M_\odot\$)')

  plt.figlegend(['Fe Core' ,'Si Shell'])
  plt.savefig('Fe_core_vs_initial_mass_log10.png')

  plt.show()
########################################################################
# All the Fe core vs Initial mass model:
  pdb.set_trace()
  all_fe_core = fe_core_z1 + fe_core_z2 + fe_core_z3 + fe_core_z4
  all_si_core = si_core_z1 + si_core_z2 + si_core_z3 + si_core_z4
  all_initial_mass = initial_mass_z1 + initial_mass_z2 + initial_mass_z3 + initial_mass_z4
  plt.figure(2)
  plt.scatter(initial_mass_z1,fe_core_z1,marker='^',color="gray",alpha=0.25)
  plt.scatter(initial_mass_z2,fe_core_z2,marker='^',color="gray",alpha=0.5)
  plt.scatter(initial_mass_z3,fe_core_z3,marker='^',color="gray",alpha=0.75)
  plt.scatter(initial_mass_z4,fe_core_z4,marker='^',color="gray",alpha=1.0)
  plt.legend(["0.0001","0.001","0.01","0.1"], title="Metallicity")
  plt.xlabel('Main Sequence Mass($M_{\odot}$)')
  plt.ylabel('Core Mass($M_{\odot}$)')
  plt.show()
###########################################################################
# Pickle the data up:
  pdb.set_trace()
  all_data = [all_fe_core , all_si_core]
  pickle.dump(all_data,open('pickle_data.p','w'))
###########################################################################



if __name__ == "__main__":
  main()
