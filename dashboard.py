# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:50:45 2022

@author: SAIJAL
"""
import os 
os.chdir("D:\\MAGDEBURG STUDIES\\WINTER_SEM_2020\\Thesis\\High_Level_Descriptors\\Evaluate_HLD_Clusters\\UI_MAKING\\Dashboard_Final")
from explainerdashboard import ExplainerDashboard



db = ExplainerDashboard.from_config("dashboard.yaml")
app = db.flask_server()

