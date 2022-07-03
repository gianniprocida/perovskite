<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1> First-principles analysis of the optical properties of lead halide perovskite solution precursors </h1>
    <hr>
       <figure>
  <img src="scheme.png" alt="counts" style="width:40%">
     </figure>
    <p> Automation and data parsing using bash scripts. Data analysis with Python. Quantum-chemistry calculations on HPC cluster
        using Gaussian. </p>
    <h2> Bash scripts </h2>
  <ul>
      <li> ParsingCpuTime.sh</li>
      <li> gaussian.job</li>
  </ul>
    <h2> Python files</h2>
    <p> (Same files) </p>
    <ul>
     <li> bromine_perovskite/lumo.py, chlorine_perovskite/lumo.py, iodine_perovskite/lumo.py (same file) </li>
      <li> bromine_perovskite/homo.py, chlorine_perovskite/homo.py, iodine_perovskite/homo.py (same file) </li>
      <li>  bromine_perovskite/uvvis.py, chlorine_perovskite/uvvis.py, iodine_perovskite/uvvis.py (same file) </li>
    </ul>
     <h2> Other files</h2>
    <ul>
     <li>  bromine_perovskite/*.out, chlorine_perovskite/*.out, iodine_perovskite/*.out </li>
      <li> bromine_perovskite/*.pdf, chlorine_perovskite/*.pdf, iodine_perovskite/*.pdf</li>
    </ul>
   </ul>
     <h2>Description</h2>
    <ul>
        <li> gaussian.job : SLURM submission script</li>
        <li> ParsingCputime.sh: It returns a file containing
             cpu time for each TD-DFT/PCM calculation located in all subdirectories of the directory in which the scripts is called
             </li>
        <li>  uvvvis.py : It plots absorption spectrum using a single TD-DFT/PCM calculation   </li>
        <li> homo.py : It pulls negative
        eigenvalues from all TD-DFT/PCM calculations of the folder in which the scripts is called.</li>
        <li> lumo.py : It pulls  positive
        eigenvalues from all TD-DFT/PCM calculations of the folder in which the scripts is called.
            chlorine_perovskite/lumo.py or iodine_perovskite/lumo.py </li>
         <li> *.out : Gaussian calculations  </li>
    </ul>
</body>


