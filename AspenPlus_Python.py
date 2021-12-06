"""
                        Aspen Plus - Python connection example 

Author: Edgar Ivan Sanchez Medina
Email: sanchez@mpi-magdeburg.mpg.de
"""

import os                          # Import operating system interface
import win32com.client as win32    # Import COM

# 1. Specify file name
file = 'Simulation\connection.bkp'

# 2. Get path to Aspen Plus file
aspen_Path = os.path.abspath(file)

# 3 Initiate Aspen Plus application
print('\n Connecting to the Aspen Plus... Please wait ')
Application = win32.Dispatch('Apwn.Document') # Registered name of Aspen Plus
print('Connected!')

# 4. Initiate Aspen Plus file
Application.InitFromArchive2(aspen_Path)

# 5. Make the files visible
Application.visible = 1

# 6. Get paths to variables of interest
# if you got problems reading string, add r at the strat of it.
 
make_up_flow = "\Data\Streams\MAKE-UP\Input\TOTFLOW\MIXED"
c7_molefrac = "\Data\Streams\C7\Output\MOLEFRAC\MIXED\HEPTANE"
 

import numpy as np
import matplotlib.pyplot as plt

# 7. Change input values in a loop and plot results
flows = np.linspace(0.0001, 1, 100)

c7_path = []

for f in flows:
    Application.Tree.FindNode(make_up_flow).Value = f
    Application.Engine.Run2()
    c7_path.append(Application.Tree.FindNode(c7_molefrac).Value)
    
plt.plot(flows, c7_path, 'bx')
plt.title('Example Aspen Plus - Python')
plt.xlabel('Make-up flowrate')
plt.ylabel('Heptane mole fraction')

# 8. Quit Aspen Plus
Application.Quit(aspen_Path)


