#!/usr/bin/python

import os
import pdb
def main():
  print("Execute all jobs")
  # cd to the star directory.
  os.chdir("/home/vtiwari/local_sw/mesa-r11554/star/")
  all_dirs = [f for f in os.listdir('.') if os.path.isdir(f)]
  for curr_dir in all_dirs:
    if "set" in curr_dir:
      #pdb.set_trace()
      os.chdir(curr_dir)
      os.system("sbatch job.mpi")
      os.chdir("..")




if __name__ == "__main__":
  main()
