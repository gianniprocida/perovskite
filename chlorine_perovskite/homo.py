import re,glob,os
import numpy as np
import pandas as pd
from functions import smallestvalues,strtofloat,concatenate_lists,largestvalues

## Create dataframe with homo,homo-1 and homo-2 for the complexes.


def HomoEnergies(fileobjects):
    solvents,lower_energies=[],[]
    for file in fileobjects:
        
        solvents.append(os.path.basename(file.name))
        for line in file:
            if 'Alpha  occ. eigenvalues' in line:
                  lines=re.findall("[+-]?\d+.\d+",line)
                  lower_energies.append(lines)
    linewithspaces=[]
    prior_lines=[]

    for i,j in enumerate(lower_energies):
          if len(j)!=5:
              linewithspaces.append(j)
              prior_lines.append(lower_energies[i-1])


    conc=concatenate_lists(linewithspaces,prior_lines)


    h_to_=list(map(strtofloat,conc))

    h_to_h2_energies=list(map(largestvalues,h_to_))


    h_to_h2=dict(zip(solvents,h_to_h2_energies))

    dataset_h=pd.DataFrame(h_to_h2)
     
    cf=27.211396
    for i in dataset_h.columns:
      dataset_h[i]=dataset_h[i]*cf   # a.u. to eV

   
    return dataset_h
