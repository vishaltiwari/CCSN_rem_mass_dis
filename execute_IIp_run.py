#!/usr/bin/python

import os
import pdb
import sys
def main():
  print("Executing the CCSN shock model")
  args = sys.argv
  os.chdir("/home/vtiwari/local_sw/mesa-r11554/star/")
  goto_dir = args[1]
  os.chdir(goto_dir)
  model_dirs = [f for f in os.listdir('.') if os.path.isdir(f)]
  for model in model_dirs:
    os.chdir(model)
    os.system('./rn')
    os.chdir('..')

if __name__ == "__main__":
  main()
