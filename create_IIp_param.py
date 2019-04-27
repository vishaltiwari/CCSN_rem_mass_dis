#!/usr/bin/python

import os
import subprocess

import re
import pdb
from string import Template

def create_runs_complie(set_name,curr_set):
  print("In the process_set call!")
  # change to the set directory:
  dir_name = "/home/vtiwari/local_sw/mesa-r11554/star/" + set_name 
  print("Changing Directory to:" + dir_name)
  os.chdir(dir_name)
  os.system("ls -al")
  # Make a copy of the example_ccsn_IIp
  model_dir_list = [f for f in os.listdir('.') if os.path.isdir(f)]
  for model in curr_set:
    print(model)
    #param = re.findall("[0-9.]+",model)
    #pdb.set_trace()
    mass =model[0]
    z = model[1]
    pre_ccsn_model_path = model[2]
    run_name = "example_ccsn_IIp_M_" + str(mass) + "_Z_" + str(z)
    #pdb.set_trace()
    # the model dir is already created skip it.
    if run_name in model_dir_list:
      continue

    #pdb.set_trace()
    cmd = "cp -r /home/vtiwari/local_sw/mesa-r11554/astro_project/example_ccsn_IIp "+run_name
    os.system(cmd)

    # copy the model here:
    os.system("cp "+pre_ccsn_model_path + " " + run_name)
    os.system("cp /home/vtiwari/local_sw/mesa-r11554/astro_project/inlist_infall.template " + run_name+"/inlist_infall")
    
    # cp the inlist_common file and change the mass and the Z value
    #d = {'mass':mass , 'z':z}
    #result = src.substitute(d)
    #out_inlist_common = open(run_name+"/"+"inlist_common","w")
    #out_inlist_common.write(result)
    #out_inlist_common.close()
    
    # change directory to that folder and execute the run
    os.chdir(run_name)
    print("Inside directory:")
    print(os.getcwd())
    os.system('./mk')
    #os.system('./rn')
    print("DONE with the compilaiton the model")
    os.chdir('../')

def convert_arg(curr_set):
  ret_str = ""
  for model in curr_set:
    ret_str = ret_str + "'" + str(model) + "' "
  return ret_str

def main():
  print("Creating the Directories for the IIp After Shock")
  cmd = 'find /home/vtiwari/local_sw/mesa-r11554/star/set_* -iname final.mod'
  results = os.popen(cmd).read().split('\n')
  
  count = 0
  sets = []
  curr_set = []
  models_per_node = 5 # number models per node:
  for paths in results:
    if paths == "":
      continue
    print(paths)
    count += 1
    model_name = paths.split('/')[-2]
    mass = re.findall('M_[0-9.]+',model_name)[0].split('_')[-1]# this is a string
    print("mass:"+mass)
    z = re.findall('Z_[0-9.]+',model_name)[0].split('_')[-1]# this is a string
    print("Z:"+z)
    
    curr_set.append((mass,z,paths))
    if count >=models_per_node:
      count = 0
      sets.append(curr_set)
      curr_set = []
      
    # open the job.mpi.template file:
  filein = open('job.mpi.template2')
    
  src = Template(filein.read())
  count = 1 
  for curr_set in sets:
    set_name = "shock_"+str(count)
    dir_name = "/home/vtiwari/local_sw/mesa-r11554/star/" + set_name
    os.system("mkdir "+dir_name)
    d = {'set_name':set_name}
    result = src.substitute(d)
      
    # write result to the file:
    job_file = open(dir_name+"/"+"job.mpi" , "w")
    job_file.write(result)
    job_file.close()
    count += 1

    create_runs_complie(set_name,curr_set)
    #pdb.set_trace()


if __name__ =="__main__":
  main()
