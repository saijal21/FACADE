# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:50:45 2022

@author: SAIJAL
"""

from explainerdashboard import ExplainerDashboard
db = ExplainerDashboard.from_config("dashboard.yaml")
app = db.flask_server()

