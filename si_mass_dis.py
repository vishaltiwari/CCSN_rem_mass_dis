#!/usr/bin/python

import pickle
import pdb

import matplotlib.pyplot as plt

def main():
  print("Fe core distribution function")
  all_data = pickle.load(open("pickle_data.p","r"))
  fe_core_masses = all_data[0]
  si_core_masses = all_data[1]
  sum_core = [e + si_core_masses[indx] for indx,e in enumerate(fe_core_masses)]
  fe_core_masses = sum_core
  min_fe_core = min(fe_core_masses)
  max_fe_core = max(fe_core_masses)
  del_mass = (max_fe_core - min_fe_core) * 0.01
  print(del_mass)
  #del_mass = 0.1 #solar
  #del_mass = 0.014 #solar
  curr_mass = min_fe_core
  mass_bin = []
  while curr_mass < max_fe_core:
    mass_bin.append(curr_mass)
    curr_mass += del_mass
  print(mass_bin)
  #pdb.set_trace()
  mass_bin_count = [0 for e in range(len(mass_bin))]
  #pdb.set_trace()
  for indx, fe_mass in enumerate(fe_core_masses):
    i = 0
    while i < len(mass_bin)-1 and fe_mass > mass_bin[i]:
      i = i + 1
    mass_bin_count[i] += 1
  #pdb.set_trace()
  # convert nu to mass fraction:
  nb_frac = [(c*1.0)/len(fe_core_masses) for c in mass_bin_count]
  f,ax = plt.subplots(1)
  plt.scatter(mass_bin , nb_frac,marker='^')
  plt.plot(mass_bin , nb_frac)
  plt.xlabel('Remnant Mass $(M_{\odot})$')
  plt.ylabel('Number of remanents')
  plt.title("Fe Core + Si Shell")
  ax.set_ylim(ymin=0)
  plt.show()

if __name__ == "__main__":
  main()
