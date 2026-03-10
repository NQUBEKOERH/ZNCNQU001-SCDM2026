# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:50:11 2026

@author: zncnqu001
"""

#importing pandas as pd
import os
import pandas as pd
#load the data file
os.chdir("C:/Users/zncnqu001/Downloads/")
df = pd.read_csv("CTD_TEMP_SALINITY_PROFILE.dat", sep = "\t")
