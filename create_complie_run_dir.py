#!/usr/bin/python
# This file with take the input argument, which is the set of all models to ecute, and will do the following:

# It will make new directory for all runs:
# copy the example_make_ccsn to cur dir name: 

import sys
import pdb
import os
import re

from string import Template

def main():
  print("In the process_set call!")
  args = sys.argv
  print(args)
  set_name = args[1]
  models = args[2:]
  # change to the set directory:
  dir_name = "../star/" + set_name 
  print("Changing Directory to:" + dir_name)
  os.chdir(dir_name)
  os.system("ls -al")

  # Make a copy of the example_make_ccsn in the current directoy
  filein = open("/home/vtiwari/mesa-r11554/CCSN_rem_mass_dis/inlist_common.template")
  src = Template(filein.read())
  for model in models:
    print(model)
    param = re.findall("[0-9.]+",model)
    mass =param[0]
    z = param[1]
    run_name = "example_make_pre_ccsn_M_" + str(mass) + "_Z_" + str(z)
    #pdb.set_trace()
    os.system("cp -r ../../CCSN_rem_mass_dis/example_make_pre_ccsn/ "+run_name)
    
    # cp the inlist_common file and change the mass and the Z value
    d = {'mass':mass , 'z':z}
    result = src.substitute(d)
    out_inlist_common = open(run_name+"/"+"inlist_common","w")
    out_inlist_common.write(result)

    # change directory to that folder and execute the run
    
    os.chdir(run_name)
    print("Inside directory:")
    print(os.getcwd())
    os.system('./mk')
    #os.system('./rn')
    print("DONE with the compilaiton the model")
    os.chdir('../')
    
if __name__ == "__main__":
  main()
