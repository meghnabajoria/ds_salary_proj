# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:37:03 2020

@author: Meghna
"""

import glassdoor_scrapper as gs
import pandas as pd
path="C:/Users/Meghna/OneDrive/Documents/ML AI Projects/ds_salary_proj/chromedriver.exe"

df=gs.get_jobs("data scientist",15,False,path,15)