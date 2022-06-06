# -*- coding: utf-8 -*-

"""
Created on Mon May  9 16:21:13 2022

@author: filip
"""

##https://colab.research.google.com/drive/1cMzZERh_lihz1nSWCV8m-HG-7b73Own5?usp=sharing

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os 
#import shutil
import goose3 as g
import numpy as np
#import requests
import datetime
#import torch
#import wget
from transformers import pipeline
#import matplotlib.pyplot as plt
#import seaborn as sns

classifier=pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-1")

candidate_labels = ["climate", "environmental","sustainable","renewable","finance"]

sentiment=pipeline("sentiment-analysis")
 

baseurl='http://data.gdeltproject.org/gkg/'

endurl='.gkg.csv.zip'
endurl_clean_article='.gkg_clean_article.csv.zip'
endurl_class='.gkg_class.csv.zip'
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
        month = '0'+ month
    if start_date.day < 10:
        day = '0'+ day
    ymd= year + month + day
    delt_zip = baseurl + ymd + endurl

    
    if  os.path.exists("F:/cleanGKG_art" +'/' +  ymd + endurl_clean_article):
        cleanGKG=pd.read_csv("F:/cleanGKG_art" +'/'+  ymd + endurl_clean_article , compression='zip')
        cleanGKG["BART_Relevant"]=pd.Series([False for x in range(len(cleanGKG.THEMES))])
        cleanGKG["BART_Finance"]=pd.Series([False for x in range(len(cleanGKG.THEMES))])
        cleanGKG["finbert_score"]=pd.Series([float("nan") for x in range(len(cleanGKG.THEMES))])
        cleanGKG["finbert_polarity"]=pd.Series([float("nan") for x in range(len(cleanGKG.THEMES))])
        cleanGKG['score_cc']=pd.Series([float("nan") for x in range(len(cleanGKG.THEMES))])
        cleanGKG['score_sus']=pd.Series([float("nan") for x in range(len(cleanGKG.THEMES))])
        cleanGKG['score_renew']=pd.Series([float("nan") for x in range(len(cleanGKG.THEMES))])
        cleanGKG['score_environmental']=pd.Series([float("nan") for x in range(len(cleanGKG.THEMES))])

        for i in range(0, len(cleanGKG.THEMES)-1):    
            try:
                src=cleanGKG.text[i]
                print(i)            
                if len(src)>500:
                    
                    results=classifier(src, candidate_labels, multi_label= True)
                    scores=(results['scores'])
                    labels=(results['labels'])
                    sequence=results['sequence']
                    idx_cc=labels.index('climate')
                    idx_sust=labels.index('sustainable')
                    idx_renew=labels.index('renewable')
                    idx_env=labels.index('environmental')
                    idx_fin=labels.index('finance')
                    
                    if scores[idx_fin] > 0.5: 
                      cleanGKG.BART_Finance[i] = True

                    if scores[idx_cc] > 0.5 or scores[idx_sust] > 0.5 or scores[idx_renew] > 0.5 or scores[idx_env] > 0.5:

                      cleanGKG.BART_Relevant[i] = True
                      cleanGKG.score_cc[i]= scores[idx_cc]
                      cleanGKG.score_sus[i]= scores[idx_sust]
                      cleanGKG.score_renew[i]= scores[idx_renew]
                      cleanGKG.score_environmental[i]= scores[idx_env]
                      
                      if cleanGKG.BART_Relevant[i] == True:                        
                        s=sequence.split('\n\n')
                        res=sentiment(s)

                        sentscore=[]
                        sentscore=[float('nan') for i in range(len(res))]

                        for j in range(len(res)):
                          subsnt=res[j]
                          sentscore[j]=subsnt['score']
                          if subsnt['label'] == 'NEGATIVE':
                            sentscore[j]=-sentscore[j]
                        
                        endscore=sum(sentscore)/len(res)
                        cleanGKG.finbert_score[i]=endscore*100
                        print(cleanGKG.finbert_score[i])

                      
            except:
                pass
      
        cleanGKG.to_csv("F:/classGKG" + '/' +  ymd + endurl_class, index=False, compression='zip')
        print('data cleaned', ymd)
        start_date += delta
    else :
        print("F:\\GKG_Raw" + '\\' +  ymd + endurl_clean_article + " does not exits!" )
        start_date += delta

        