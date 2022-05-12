# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:08:26 2022

@author: filip
"""
import warnings
warnings.filterwarnings('ignore')
#import pandas as pd
import os 
#import shutil
#import goose3
#import numpy as np
#import requests
import datetime
import wget


baseurl='http://data.gdeltproject.org/gkg/'

endurl='.gkg.csv.zip'

start_date = datetime.date(2020, 1, 30)
end_date = datetime.date(2022, 5, 4)
delta = datetime.timedelta(days=1)
match=0 

while start_date <= end_date:
    year=str(start_date.year)    
    month=str(start_date.month)
    day=str(start_date.day)
    
    if start_date.month < 10:
        month = '0'+month
    if start_date.day < 10:
        day = '0'+day
    ymd=year+month+day
    delt_zip=baseurl+ymd+endurl
    if not os.path.exists("F:\\GKG_Raw" + '\\' +  ymd + endurl):
        wget.download(delt_zip, out='F:\\GKG_Raw')
        start_date += delta
    else :
        print("F:\\GKG_Raw" + '\\' +  ymd + endurl + " already exits!" )
        start_date += delta
print("Downloading finished")
 

