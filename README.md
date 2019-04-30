# Core Collapse Supernova Remnant Mass Distribution

## About:
Stars having mass more that 11 Solar Masses undergo core-collapse supernova explosion, and leaves behind a compact objects, either a neutron star or a black hole, which would depend on the initial mass and the initial metallicity of the progenitor star.
In this project I have explored the mass distribution function of the Fe core and inner shell masses using the MESA stellar code.
Exploration of Mass Distribution function of Black holes and Neutron Stars using Mesa Stellar Evolution Code[3]. The work is based on the work by Timmes.et.al[1].

## Parameter Exploration
- Initial Mass: [16-50] Solar Masses.
- Initial Metallictiy: [10^-4 , 10^-3, 10^-2 , 10^-1]

## Mesa Models:
The following models from MESA were used during the study:
TODO: Write a brief description of both the models used:
- 25M_pre_ms_to_core_collapse:
- example_ccsn_IIp:

## Computational Framework:
To explore such a big parameter space, running indiviaul models is not feiasialbe, so I developed a framework where I could submit multiple models to be computeded over various nodes on carnie(UMass Dartmouth computer cluster). This is described as below:

- The parameter space which has number(Initial_masses) X number(Initial_metallicity) points, is subdivided into sets of 15 models  per set.
- For each set, a seperate directory is created, which will contain seperate directories for each of the its models.
- In each these models directory is a copy of the directory "25M_pre_ms_to_core_collapse". The directory name is marked with a label M_<M_value>_Z<Z_Value> at the end of its name.
- Each of these model directories have initial_mass and initial_z in the list_common file, which is copied into these directories by making use of a template file. this allows for varying the parameters for different models.
- At the end each model directory is complied using the './mk'.

- Each set directory, also contains a SBATCH submission script(to be run on a single node), which will execute the './rn' inside each of the model directories in order.

- A total of 20 sets were created. Each set was submitted to a particular node having 48 hardware threads(24 cores).

- Main Codes: create_param_sets.py, execute_run.py, create_IIp_param.py,execute_IIp_run.py, execute_jobs.py

![FrameWork](https://raw.githubusercontent.com/vishaltiwari/CCSN_rem_mass_dis/master/images/Framework_astro_project.png)


## Results:

## References:
[1] Timmes, F. X., S. E. Woosley, and Thomas A. Weaver. "The neutron star and black hole initial mass function." arXiv preprint astro-ph/9510136 (1995). 

[2] Woosley, S. E., and Thomas A. Weaver. The evolution and explosion of massive Stars II: Explosive hydrodynamics and nucleosynthesis. No. UCRL-ID-122106. Lawrence Livermore National Lab., CA (United States), 1995. 

[3] Paxton, Bill, et al. "Modules for Experiments in Stellar Astrophysics (): Convective Boundaries, Element Diffusion, and Massive Star Explosions." The Astrophysical Journal Supplement Series 234.2 (2018): 34.
