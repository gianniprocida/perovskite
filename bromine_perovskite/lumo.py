import re,glob,os
import numpy as np
import pandas as pd
from functions import smallestvalues,strtofloat,concatenate_lists
from homo import HomoEnergies


## Create dataframe with lumo,lumo+1 and lumo+2 for the complexes.

output=[]

for file in glob.glob("*.out"):
 output.append(file)

fileobjects=[open(f,'r') for f in output]


solvents,upper_energies=[],[]
for file in fileobjects:
    solvents.append(os.path.basename(file.name))
# Store only one line for each file as list of lists
    for line in file:
       if 'Alpha virt. eigenvalues' in line:
            break
    lines=re.findall("[+-]?\d+.\d+",line)
    upper_energies.append(lines)

    

#Convert to float

l_to_=list(map(strtofloat,upper_energies))


#Pulll n largest energies 
l_to_l2_energies=list(map(smallestvalues,l_to_))

#Create dictionary
l_to_l2=dict(zip(solvents,l_to_l2_energies))

# Dataframe

dataset_l=pd.DataFrame(l_to_l2)
 
cf=27.211396
for i in dataset_l.columns:
  dataset_l[i]=dataset_l[i]*cf   # a.u. to eV

print(dataset_l)
#########



output=[]

for file in glob.glob("*.out"):
 output.append(file)

fileobjects=[open(f,'r') for f in output]

dataset_h=HomoEnergies(fileobjects)

