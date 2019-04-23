#!/usr/bin/python

import pdb
import os
from string import Template

def create_runs_complie(set_name,curr_set):
  print("In the process_set call!")
  # change to the set directory:
  dir_name = "/home/vtiwari/local_sw/mesa-r11554/star/" + set_name 
  print("Changing Directory to:" + dir_name)
  os.chdir(dir_name)
  os.system("ls -al")
  # Make a copy of the example_make_ccsn in the current directoy
  filein = open("/home/vtiwari/mesa-r11554/CCSN_rem_mass_dis/inlist_common.template")
  src = Template(filein.read())
  model_dir_list = [f for f in os.listdir('.') if os.path.isdir(f)]
  for model in curr_set:
    print(model)
    #param = re.findall("[0-9.]+",model)
    #pdb.set_trace()
    mass =model[0]
    z = model[1]
    run_name = "example_make_pre_ccsn_M_" + str(mass) + "_Z_" + str(z)
    #pdb.set_trace()
    # the model dir is already created skip it.
    if run_name in model_dir_list:
      continue

    #os.system("cp -r /home/vtiwari/mesa-r11554/astro_project/example_make_pre_ccsn/ "+run_name)
    os.system("cp -r /home/vtiwari/mesa-r11554/CCSN_rem_mass_dis/25M_pre_ms_to_core_collapse "+run_name)
    
    # cp the inlist_common file and change the mass and the Z value
    d = {'mass':mass , 'z':z}
    result = src.substitute(d)
    out_inlist_common = open(run_name+"/"+"inlist_common","w")
    out_inlist_common.write(result)
    out_inlist_common.close()
    
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
  print("Main")
  init_masses = [e+11 for e in range(40)]
  init_Zs = [0.0001, 0.001 ,0.01, 0.1, 1, 1.1 ,1.5,2.0]
  sets = []
  curr_set = []
  models_per_node = 15 # number models per node:
  count = 0 
  for M in init_masses:
    for Z in init_Zs:
      curr_set.append((M,Z))
      count += 1
      if count >= models_per_node:
        count = 0
        sets.append(curr_set)
	curr_set = []
  
  # open the job.mpi.template file:
  filein = open('job.mpi.template')
  src = Template(filein.read())
  count = 1

  for curr_set in sets:
    set_name = "set_"+str(count)
    dir_name = "/home/vtiwari/local_sw/mesa-r11554/star/" + set_name
    os.system("mkdir "+dir_name)
    #pdb.set_trace()
    d = {'set_name':set_name , 'set_arg':convert_arg(curr_set)}
    result = src.substitute(d)
    # write result to the file:
    job_file = open(dir_name+"/"+"job.mpi" , "w")
    job_file.write(result)
    job_file.close()
    count += 1
    #pdb.set_trace()
    #create_runs_complie(set_name,curr_set)

    # execute the runs:
    #pdb.set_trace()
    #os.chdir(dir_name)
    #print("Entering dir:" + dir_name)
    #print("Submitting the job")
    #os.system("sbatch job.mpi")
    #print("Job submitted\n")
    #os.chdir("../")

   

if __name__ == "__main__":
  main()
