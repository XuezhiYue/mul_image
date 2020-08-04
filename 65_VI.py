#!/Users/wxl/anaconda3/bin/python3.7
# -*- coding: utf-8 -*-
"""
  @Author  : Yxz
  @contact: yuexuezhi091@gmail.com
  @Software: PyCharm
  @FileName: 65_VI.py
  @Time    : 2020/7/24 11:30
  @desc:
"""

import os

import csv
VI_list = []

reader = ['GRVI', 'GDVI', 'GNDVI', 'GWDRVI', 'CIg', 'MSR_G', 'GSAVI', 'MGSAVI', 'GOSAVI', 'GRDVI', 'NDVI', 'RVI', 'OSAVI', 'WDRVI', 'SAVI', 'MSAVI', 'DVI', 'RDVI', 'TNDVI', 'MSR', 'VIopt', 'MERIS', 'RERVI', 'REDVI', 'NDRE', 'RERDVI', 'REWDRVI', 'VIopt1', 'CIre', 'MSR_RE', 'RESAVI', 'MRESAVI', 'REOSAVI', 'NDRE_REOSAVI', 'SR', 'RDVI1', 'RENDVI', 'REGRVI', 'REGDVI', 'REGNDVI', 'MTCI', 'DATT', 'NGI', 'NREI', 'NRI', 'NNIR', 'MDD', 'MNDI', 'MEVI', 'MNDRE', 'MCARI1', 'MCARI2', 'MCARI1_REOSAVI', 'MCARI2_REOSAVI', 'MTCARI', 'MTCARI_REOSAVI', 'RETVI', 'MRETVI', 'NDRE_GOSAVI', 'MCCCI', 'MTCARI_MRETVI', 'MTCARI_GOSAVI', 'MCARI2_GOSAVI', 'MCARI1_MRETVI', 'MCARI1_GOSAVI']


print(reader)