#!/usr/bin/env python
# coding: utf-8

# Temporada 19/20 de la WSL

# In[1]:


import pandas as pd
wsl=pd.read_json('https://raw.githubusercontent.com/gonzalo09002/open-data/81bb27062e43874a1bdb72be9d243e93a8212dbc/data/matches/37/42.json')
wsl=wsl.drop(columns=['competition','season','metadata','competition_stage','stadium','referee'])
wsl.head(10)

