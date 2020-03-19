""" 
    This script runs hyper paramtetrization on the simulations. 

    The objective is to collect data 

"""

# ======================================================================================================================
# Imports
# ======================================================================================================================

import papermill as pm
from itertools import product

# ======================================================================================================================
# Contants
# ======================================================================================================================

PRB = (0.0, 0.1, 0.2, 0.3, 0.5, 0.7)
CTR = ("MANUAL",)
Z = ("Cpt_5",)
D = (50,)

cases = product(PRB, CTR, Z, D)
# for case in cases:
#     print(case)gt

# ======================================================================================================================
# Runtime
# ======================================================================================================================

for case in cases:
    pvan, ctr_type, zone, dst = case
    print(case)
    pm.execute_notebook(
        "01_Zone_Characterisation.ipynb",
        "01_Zone_Characterisation.ipynb",
        parameters=dict(VANISHING=pvan, CONTROL_TYPE=ctr_type, ZONE=zone, DISTANCE_CONTROL=dst),
    )
