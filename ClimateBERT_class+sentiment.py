# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:21:13 2022

@author: filip
"""

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os 
#import shutil
import goose3 as g
import numpy as np
#import requests
import datetime
import torch
#import wget
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns


classifier=pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-1")
candidate_labels = ['renewable',"energy", "economy", "climate change", "sustainability", "climate finance", "opinion"]





baseurl='http://data.gdeltproject.org/gkg/'

endurl='.gkg.csv.zip'
endurl_clean='.gkg_clean.csv.zip'

start_date = datetime.date(2013, 4, 1)
end_date = datetime.date(2013, 4, 1)
delta = datetime.timedelta(days=1)
match=0 
goose = g.Goose()

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
    if  os.path.exists("F:\\cleanGKG" + '\\' +  ymd + endurl_clean):
        cleanGKG=pd.read_csv("F:\\cleanGKG" + '\\' +  ymd + endurl_clean , compression='zip', delimiter= '\t')
        cleanGKG.BERT_Class=pd.Series([float("nan") for x in range(len(cleanGKG.index))])
        cleanGKG.BERT_Sent=pd.Series([float("nan") for x in range(len(cleanGKG.index))])
        for i in range(0, len(cleanGKG.THEMES)-1):    
            src=goose.extract(cleanGKG.SOURCEURL[i])
            if len(src.cleaned_text)>300:
                results=classifier(src.cleaned_text, candidate_labels)
        start_date += delta
    else :
        print("F:\\GKG_Raw" + '\\' +  ymd + endurl_clean + " does not  exits!" )
        start_date += delta
print(results)
 