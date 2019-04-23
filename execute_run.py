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
  print("In the Execute call!")
  args = sys.argv
  print(args)
  set_name = args[1]
  models = args[2:]
  # change to the set directory:
  dir_name = "../star/" + set_name 
  print("Changing Directory to:" + dir_name)
  os.chdir(dir_name)
  #os.system("ls -al")

  # Make a copy of the example_make_ccsn in the current directoy
  model_dirs = [f for f in os.listdir('.') if os.path.isdir(f)]
  for model_dir in model_dirs:
    print("EXECUTING MODEL:")
    print(model_dir)
    os.chdir(model_dir)
    
    print("Inside directory:")
    print(os.getcwd())
    print("Executing:")
    #os.system('./rn')
    print("DONE with executing the model")
    os.chdir('../')
    
if __name__ == "__main__":
  main()
