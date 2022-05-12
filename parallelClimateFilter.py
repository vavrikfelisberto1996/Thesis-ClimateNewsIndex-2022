# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:07:46 2022

@author: filip
"""
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os 
import datetime
import concurrent.futures
"""
define filter fn
"""
def parfilter(S):
    G_C=False 
    G_F=False 
    G_E=False 
    G_CD=False 
    G_EPM=False 
    G_EH=False 
    G_CS=False 
    G_Econ=False 
    G_RE=False
    for k in range(0, S.size-1):
                    if (S[k][0] == ('WB_567_CLIMATE_CHANGE' )) == True :
                        G_C=True
                       
                    if (S[k][0] == (                     'ENV_CLIMATECHANGE')) == True :
                        G_C=True
                       
                    if (S[k][0] == (                     'UNGP_CLIMATE_CHANGE_ACTION')) == True :
                        G_C=True
                        
                    if (S[k][0] == (                     'WB_579_CLIMATE_CHANGE_MITIGATION' )) == True :
                        G_C=True
                       
                    if (S[k][0] == (                     'WB_1841_SHORT_LIVED_CLIMATE_POLLUTANTS'  )) == True :
                        G_C=True
                       
                    if (S[k][0] == (                    'WB_1773_CLIMATE_CHANGE_IMPACTS'  )) == True :
                        G_C=True
                       
                    if (S[k][0] == (                    'WB_574_CLIMATE_CHANGE_ADAPTATION'  )) == True :
                        G_C=True
                       
                    if (S[k][0] == (                     'WB_959_CLIMATE_CHANGE_LAW')) == True :
                        G_C=True
                       
                    if (S[k][0] == (                    'WB_747_SOCIAL_RESILIENCE_AND_CLIMATE_CHANGE')) == True :
                        G_C=True
                       
                    if (S[k][0] == (                  'WB_1839_OZONE_LAYER_DEPLETION_AND_CLIMATE_CHANGE')) == True :
                        G_C=True
                       
                    if (S[k][0] == (                  'WB_575_COMMUNITY_BASED_CLIMATE_ADAPTATION')) == True :
                        G_C=True
                       
                    if (S[k][0] == (                   'WB_1750_CLIMATE_CHANGE_ADAPTATION_IMPACTS'
                                        )) == True :
                        G_C=True
                       
                        




                    if (S[k][0] == ('WB_1847_CLIMATE_FINANCE'	)) == True :
                        G_F=True
                         
                    if (S[k][0] == ('WB_1844_MARKET_BASED_CLIMATE_CHANGE_MITIGATION')) == True :
                        G_F=True
                        
                    if (S[k][0] == ('WB_573_CLIMATE_RISK_MANAGEMENT')) == True :
                        G_F=True
                        
                    if (S[k][0] == ('WB_1849_PUBLIC_CLIMATE_FINANCE')) == True :
                        G_F=True
                        
                    if (S[k][0] == ('WB_1850_PRIVATE_CLIMATE_FINANCE')) == True :
                        G_F=True
                        
                    if (S[k][0] == ('WB_1838_CLIMATE_RISK_SCREENING')) == True :
                        G_F=True
                        
                    if (S[k][0] == ('WB_582_GREENHOUSE_GAS_ACCOUNTING'
                                          )) == True :
                        G_F=True
                        


                    if  (S[k][0] == ('ENV_WINDPOWER'))== True: 
                      G_E=True
                      
                    if  (S[k][0] == ('ENV_SOLAR' ))== True:
                      G_E=True
                      
                    if  (S[k][0] == ('ENV_HYDRO' ))== True:
                      G_E=True
                      
                    if  (S[k][0] == ('ENV_BIOFUEL' ))== True:
                      G_E=True
                      
                    if  (S[k][0] == ('ENV_GEOTHERMAL'))== True:
                      G_E=True
                      
                    if  (S[k][0] == ('WB_525_RENEWABLE_ENERGY'))== True:
                      G_E=True
                      
                                          
                        

                        
                    # if (S == ('ENV_METALS'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (S == ('ENV_MINING'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (S == ('ENV_FISHERY'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (S == ('ENV_FORESTRY'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (S == ('ENV_WATERWAYS'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (S == ('WB_566_ENVIRONMENT_AND_NATURAL_RESOURCES'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (S == ('WB_897_MINING_ENVIRONMENTAL_MANAGEMENT'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (S == ('ENV_DEFORESTATION' ))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (S == ('ENV_OVERFISH'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       



                    if (S[k][0] == ( 'MANMADE_DISASTER_ENVIRONMENTAL_DISASTER'))==True:
                        G_CD=True
                        
                    if (S[k][0] == ( 'WB_1831_ENVIRONMENTAL_CRIME_AND_LAW_ENFORCEMENT'))==True:
                        G_CD=True
                        
                    if (S[k][0] == ('WB_2916_ENVIRONMENTAL_LAW_ENFORCEMENT'))==True:
                        G_CD=True
                        
                    if (S[k][0] == ('WB_2915_ENVIRONMENTAL_CRIME'))==True:
                        G_CD=True
                       
                    if (S[k][0] == ('MANMADE_DISASTER_MARITIME_ENVIRONMENTAL_DISASTER'))==True:
                        G_CD=True
                        
                    if (S[k][0] == ('SELF_IDENTIFIED_ENVIRON_DISASTER'))==True:
                        G_CD=True
                        
                    if ([k][0] == ('WB_1936_ENVIRONMENTAL_CRIME_ENFORCEMENT'))==True:
                        G_CD=True
                       
                            
                       


                    if (S[k][0] ==('WB_901_ENVIRONMENTAL_SAFEGUARDS'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_849_ENVIRONMENTAL_LAWS_AND_REGULATIONS'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_1785_ENVIRONMENTAL_POLICIES_AND_INSTITUTION'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'ECON_DEVELOPMENTORGS_UNITED_NATIONS_ENVIRONMENT_PROGRAMME'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_1782_ENVIRONMENTAL_AGREEMENTS_AND_CONVENTIONS'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_1783_ENVIRONMENTAL_GOVERNANCE'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_2307_ENVIRONMENTAL_MANAGEMENT_AND_MITIGATION_PLANS'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_2306_ENVIRONMENTAL_IMPACT_ASSESSEMENT'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_1376_ENVIRONMENTAL_OFFSETS'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_157_ENVIRONMENTAL_WATER_USE_AND_CATCHMENT_PROTECTION'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_1378_PAYMENT_FOR_ENVIRONMENT_SERVICES'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_2195_ENVIROMENTAL_IMPACT_ASSESSMENT'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_598_ENVIRONMENTAL_MANAGEMENT'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_526_RENEWABLE_ENERGY_POLICY_AND_REGULATION'))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_1057_SUSTAINABLE_FOREST_MANAGEMENT'
                            ))== True:
                        G_EPM=True
                        
                    if (S[k][0] ==( 'WB_1792_ENVIRONMENTAL_HEALTH'))== True:
                        G_EH=True
                        
                    if (S[k][0] ==( 'WB_1717_URBAN_POLLUTION_AND_ENVIRONMENTAL_HEALTH'
                            ))== True:
                        G_EH=True
                        
                    if (S[k][0] ==('WB_2197_ENVIRONMENTAL_ENGINEERING'))== True:
                        G_CS = True
                        
                    if (S[k][0] ==( 'ENV_CARBONCAPTURE'))== True:
                        G_CS = True
                        
                    if (S[k][0] ==( 'WB_571_CLIMATE_SCIENCE'))== True:
                        G_CS = True
                        
                    if (S[k][0] ==( 'WB_1784_ENVIRONMENTAL_INFORMATION_MANAGEMENT'))== True:
                        G_CS = True
                        
                    if (S[k][0] ==( 'WB_399_INNOVATION_FOR_GREEN_GROWTH'
                            ))== True:
                        G_CS = True
                        
                        



                    if (S[k][0] == ( 'WB_476_GREEN_GROWTH'  ))== True:
                       G_Econ = True          
                                            
                    if (S[k][0] == ( 'WB_2674_GREEN_JOBS'))== True:
                       G_Econ = True          
                        
                    if (S[k][0] == ('WB_1100_SUSTAINABLE_GROWTH'))== True:
                       G_Econ = True          
                        
                    if (S[k][0] == ( 'WB_1856_TRADE_AND_THE_ENVIRONMENT'))== True:
                       G_Econ = True          
                        
                    if (S[k][0] == ( 'WB_791_TRANSPORT_IMPACT_ON_THE_ENVIRONMENT'))== True:
                       G_Econ = True          
                        
                            


                    if (S[k][0] == ( 'WB_802_GREEN_CITIES'))== True:
                        G_RE = True
                        
                    if (S[k][0] == ('WB_408_GREEN_BUILDINGS' ))== True:
                        G_RE = True
                    
                    output=[G_C, G_F, G_E, G_CD, G_EPM, G_EH, G_CS, G_Econ, G_RE]
                    
                            
                    return output


start_date = datetime.date(2013, 5, 1)
end_date = datetime.date(2013, 8, 1)
delta = datetime.timedelta(days=1)
endurl='.gkg.csv.zip'
endurl_clean='.gkg_clean.csv.zip'

while start_date <= end_date:
    year=str(start_date.year)    
    month=str(start_date.month)
    day=str(start_date.day)
    
    if start_date.month < 10:
        month = '0'+month
    if start_date.day < 10:
        day = '0'+day
    ymd=year+month+day

    if os.path.exists("F:\\GKG_Raw" + '\\' +  ymd + endurl) and not os.path.exists("F:\\cleanGKG" + '\\' +  ymd + endurl_clean):
        GKG_=pd.read_csv("F:\\GKG_Raw" + '\\' +  ymd + endurl , compression='zip', delimiter= '\t')


        GKG_['Climate_Change'] = pd.Series([False for x in range(len(GKG_.index))])
        GKG_['Climate_Finance']= pd.Series([False for x in range(len(GKG_.index))])
        GKG_['GREEN_ENERGY']= pd.Series([False for x in range(len(GKG_.index))])
        #GKG_['BROWN_ENERGY']= pd.Series([False for x in range(len(GKG_.index))])
        GKG_['NAT_RES']= pd.Series([False for x in range(len(GKG_.index))])
        GKG_['CRIMEDISASTER']= pd.Series([False for x in range(len(GKG_.index))])
        GKG_['EnvHealth']= pd.Series([False for x in range(len(GKG_.index))])
        GKG_['ENV_POL_MAN']= pd.Series([False for x in range(len(GKG_.index))])
        GKG_['Climate_Science']= pd.Series([False for x in range(len(GKG_.index))])
        GKG_['Urban_RE']= pd.Series([False for x in range(len(GKG_.index))])
        GKG_['Green_Econ']= pd.Series([False for x in range(len(GKG_.index))])



        for i in range(0, len(GKG_.THEMES)-1):
            s=pd.Series(GKG_.THEMES[i])
            tof=s.isna()
            
            if  tof[0]==True:     
                pass
            else:
                split=s.str.split(r";", expand=True)
                
                out = parfilter(split)
                print(out)
                if out is None:
                    out=[False,False,False,False,False,False,False,False,False]
                    
                GKG_['Climate_Change'][i]=out[0] 
                GKG_['Climate_Finance'][i]=out[1]  
                GKG_['GREEN_ENERGY'][i]=out[2] 
                GKG_['CRIMEDISASTER'][i]=out[3] 
                GKG_['ENV_POL_MAN'][i]=out[4] 
                GKG_['EnvHealth'][i]=out[5] 
                GKG_['Climate_Science'][i]=out[6]  
                GKG_['Green_Econ'][i]=out[7] 
                GKG_['Urban_RE'][i]=out[8] 
        
        
        
        GKG_['flag'] = pd.Series([False for x in range(len(GKG_.index))])
        GKG_['flag'] = GKG_['Climate_Change'] + GKG_['Climate_Finance'] 
        + GKG_['GREEN_ENERGY'] + GKG_['NAT_RES'] + GKG_['CRIMEDISASTER'] 
        + GKG_['EnvHealth'] + GKG_['ENV_POL_MAN'] + GKG_['Climate_Science'] 
        + GKG_['Urban_RE']+GKG_['Green_Econ']

        cleanGKG = GKG_[GKG_['flag']>0]
        del cleanGKG['DATE']
        del cleanGKG['COUNTG_RE']
        del cleanGKG['LOCATIONS']
        del cleanGKG['PERSONS']
        del cleanGKG['CAMEOEVENTIDS']
        del cleanGKG['flag']

        cleanGKG.to_csv("F:\\cleanGKG" + '\\' +  ymd + endurl_clean, index=False, compression='zip')
        print('data cleaned', ymd)
        start_date += delta
    else :
        print("F:\\cleanGKG" + '\\' +  ymd + endurl + " does not exist! or already processed" )
        start_date += delta























# goose = Goose()

# i = 1
# src=goose.extract(results.SOURCEURL[i])
# nsrc=results.NumSources[i]
# tags = src.tags
# keywords =src.meta_keywords 
# domain=src.domain
# print(tags)
# print(keywords)
# #    if src.meta_lang ~= 'en' &  len(src.cleaned_text) < 300 :
    