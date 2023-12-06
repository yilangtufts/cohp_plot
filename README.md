# COHP Plot Generator

## Overview

The `cohp_plot.py` script is used to generate COHP (Crystal Orbital Hamilton Population) plots for selected atom pairs. These plots provide insights into the bonding characteristics between specified atoms in a material.  

## Usage
Under the directory of COHPCAR.lobster that you want to use for COHP plots  
cohp_plot.py [-h] [-a atom_pairs [atom_pairs ...]] [-c colors [colors ...]] [-f filename]  

## Options
-h, --help: Show the help message and exit.  
-a, --atom_pairs: Specify atom pairs for COHP plots. Separate atom symbols with a hyphen, and list multiple pairs if needed. Example: O-Pt, Si-Pt, Zn-Pt.  
-c, --colors: Define colors for the plots. Provide color names or codes, and match them with the corresponding atom pairs. Example: red, gold, blue.  
-f, --filename: Specify the output file name for the generated plots. Example: cohp.  

## Example usage
`cohp_plot.py -a O-Pt Si-Pt Zn-Pt -c red gold blue -f cohp`  
This will plot the COHP between O and Pt, Si and Pt, Zn and Pt, with colors of red, gold, blue, respectively, and will save a png image named "cohp".  
