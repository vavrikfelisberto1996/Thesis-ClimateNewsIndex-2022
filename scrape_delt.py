import numpy as np
import pandas as pd
import gdelt 
import goose3 
import torch 
import os 
import wget
from goose3 import article
from goose3 import Goose 


gd2 = gdelt.gdelt(version=1)
results = gd2.Search(['2020 04 01'], table='events')
print(len(results))


goose = Goose()

i = 1
src=goose.extract(results.SOURCEURL[i])
nsrc=results.NumSources[i]
tags = src.tags
keywords =src.meta_keywords
domain=src.domain
print(tags)
print(keywords)
#    if src.meta_lang ~= 'en' &  len(src.cleaned_text) < 300 :
    