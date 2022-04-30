# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:08:26 2022

@author: filip
"""
import pandas as pd
import os 
import shutil
import goose3
import numpy as np
import requests
import datetime
import wget


baseurl='http://data.gdeltproject.org/gkg/'

endurl='.gkg.csv.zip'

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 1, 1)
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
        wget.download(delt_zip, out='F:\GKG_Raw')
    else :
        print("F:\\GKG_Raw" + '\\' +  ymd + endurl + " already exits!" )
        start_date += delta
print("Downloading finished")
 
GKG_=pd.read_csv("F:\\GKG_Raw" + '\\' +  ymd + endurl , compression='zip', delimiter= '\t')

GKG_['Climate_Change'] = pd.Series([False for x in range(len(GKG_.index))])
GKG_['Climate_Finance']= pd.Series([False for x in range(len(GKG_.index))])
GKG_['Urban']= pd.Series([False for x in range(len(GKG_.index))])
GKG_['ECON']= pd.Series([False for x in range(len(GKG_.index))])
GKG_['GREEN_ENERGY']= pd.Series([False for x in range(len(GKG_.index))])
GKG_['BROWN_ENERGY']= pd.Series([False for x in range(len(GKG_.index))])
GKG_['INNO']= pd.Series([False for x in range(len(GKG_.index))])
GKG_['ENV']= pd.Series([False for x in range(len(GKG_.index))])

for i in range(0, len(GKG_.THEMES)-1):
    i=i
    s=pd.Series(GKG_.THEMES[i])
    tof=s.isna()
    if  tof[0]==True:     
        pass
    else:
        split=s.str.split(r";", expand=True)
        for k in range(0, split.size-1):
            if (split[k][0] == ('WB_567_CLIMATE_CHANGE' 
                                or 'ENV_CLIMATECHANGE'
                                or 'UNGP_CLIMATE_CHANGE_ACTION' 
                                or 'WB_579_CLIMATE_CHANGE_MITIGATION'
                                or 'WB_571_CLIMATE_SCIENCE' 
                                or 'WB_1841_SHORT_LIVED_CLIMATE_POLLUTANTS'
                                or 'WB_1773_CLIMATE_CHANGE_IMPACTS'
                                or 'WB_574_CLIMATE_CHANGE_ADAPTATION'
                                or 'WB_959_CLIMATE_CHANGE_LAW'
                                or 'WB_747_SOCIAL_RESILIENCE_AND_CLIMATE_CHANGE'
                                or 'WB_1839_OZONE_LAYER_DEPLETION_AND_CLIMATE_CHANGE'
                                or 'WB_575_COMMUNITY_BASED_CLIMATE_ADAPTATION'
                                or 'WB_1750_CLIMATE_CHANGE_ADAPTATION_IMPACTS')) == True :
                GKG_['Climate_Change'][i]=True
                
            elif (split[k][0] == ('WB_1847_CLIMATE_FINANCE'	 
                                  or 'WB_1844_MARKET_BASED_CLIMATE_CHANGE_MITIGATION'
                                  or 'WB_573_CLIMATE_RISK_MANAGEMENT'
                                  or 'WB_1849_PUBLIC_CLIMATE_FINANCE'
                                  or 'WB_1850_PRIVATE_CLIMATE_FINANCE'
                                  or 'WB_1838_CLIMATE_RISK_SCREENING'
                                  or 'WB_582_GREENHOUSE_GAS_ACCOUNTING'
                                  )) == True :
                GKG_['Climate_Finance'][i]=True
        
            elif  (split[k][0] == ('' ))== True:
                GKG_['ECON'][i]=True
        

            elif  (split[k][0] == ('ENV_WINDPOWER' 
                                   or 'ENV_SOLAR' 
                                   or 'ENV_HYDRO' 
                                   or 'ENV_BIOFUEL' 
                                   or 'ENV_GEOTHERMAL'))== True:
                GKG_['GREEN_ENERGY'][i]=True
            
                
            
            
            
            
            
            
ENV_OIL
ENV_MINING
ENV_COAL
ENV_NATURALGAS
ENV_METALS
ENV_FISHERY
ENV_FORESTRY

ENV_WATERWAYS

WB_566_ENVIRONMENT_AND_NATURAL_RESOURCES
WB_598_ENVIRONMENTAL_MANAGEMENT

ENV_SPECIESENDANGERED (CONDITIONAL)
ENV_NUCLEARPOWER
ENV_DEFORESTATION
WB_901_ENVIRONMENTAL_SAFEGUARDS

WB_849_ENVIRONMENTAL_LAWS_AND_REGULATIONS
WB_2197_ENVIRONMENTAL_ENGINEERING
WB_1785_ENVIRONMENTAL_POLICIES_AND_INSTITUTION
SELF_IDENTIFIED_ENVIRON_DISASTER
WB_1792_ENVIRONMENTAL_HEALTH
ENV_CARBONCAPTURE
ENV_OVERFISH
WB_1388_ENVIRONMENTAL_AND_SOCIAL_ASSESSMENTS (CONDITIONAL)
MANMADE_DISASTER_ENVIRONMENTAL_DISASTER
WB_1831_ENVIRONMENTAL_CRIME_AND_LAW_ENFORCEMENT
WB_1717_URBAN_POLLUTION_AND_ENVIRONMENTAL_HEALTH
WB_2915_ENVIRONMENTAL_CRIME

ENV_SPECIESEXTINCT (CONDITIONAL)

TAX_FNCACT_ENVIRONMENTAL_SCIENTIST
ECON_DEVELOPMENTORGS_UNITED_NATIONS_ENVIRONMENT_PROGRAMME
WB_2916_ENVIRONMENTAL_LAW_ENFORCEMENT
WB_1782_ENVIRONMENTAL_AGREEMENTS_AND_CONVENTIONS
WB_1783_ENVIRONMENTAL_GOVERNANCE
WB_2307_ENVIRONMENTAL_MANAGEMENT_AND_MITIGATION_PLANS
WB_2306_ENVIRONMENTAL_IMPACT_ASSESSEMENT
WB_1376_ENVIRONMENTAL_OFFSETS
TAX_DISEASE_ENVIRONMENTAL_ILLNESS
WB_897_MINING_ENVIRONMENTAL_MANAGEMENT	
MANMADE_DISASTER_MARITIME_ENVIRONMENTAL_DISASTER
WB_1784_ENVIRONMENTAL_INFORMATION_MANAGEMENT
WB_1856_TRADE_AND_THE_ENVIRONMENT
WB_1936_ENVIRONMENTAL_CRIME_ENFORCEMENT
WB_157_ENVIRONMENTAL_WATER_USE_AND_CATCHMENT_PROTECTION
WB_1378_PAYMENT_FOR_ENVIRONMENT_SERVICES
WB_2195_ENVIROMENTAL_IMPACT_ASSESSMENT
WB_791_TRANSPORT_IMPACT_ON_THE_ENVIRONMENT
