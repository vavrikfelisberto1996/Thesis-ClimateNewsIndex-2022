import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os 
import datetime
#import concurrent.futures

start_date = datetime.date(2013, 4, 11)
end_date = datetime.date(2021, 12, 31)
delta = datetime.timedelta(days=1)
endurl='.gkg.csv.zip'
endurl_clean='.gkg_clean.csv.zip'

while start_date <= end_date:
    year=str(start_date.year)    
    month=str(start_date.month)
    day=str(start_date.day)
    
    if start_date.month < 10:
        month = '0' + month
    if start_date.day < 10:
        day = '0' + day
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
                for k in range(0, split.size-1):
                    if (split[k][0] == ('WB_567_CLIMATE_CHANGE' )) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                     'ENV_CLIMATECHANGE')) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                     'UNGP_CLIMATE_CHANGE_ACTION')) == True :
                        GKG_['Climate_Change'][i]=True
                        
                    if (split[k][0] == (                     'WB_579_CLIMATE_CHANGE_MITIGATION' )) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                     'WB_1841_SHORT_LIVED_CLIMATE_POLLUTANTS'  )) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                    'WB_1773_CLIMATE_CHANGE_IMPACTS'  )) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                    'WB_574_CLIMATE_CHANGE_ADAPTATION'  )) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                     'WB_959_CLIMATE_CHANGE_LAW')) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                    'WB_747_SOCIAL_RESILIENCE_AND_CLIMATE_CHANGE')) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                  'WB_1839_OZONE_LAYER_DEPLETION_AND_CLIMATE_CHANGE')) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                  'WB_575_COMMUNITY_BASED_CLIMATE_ADAPTATION')) == True :
                        GKG_['Climate_Change'][i]=True
                       
                    if (split[k][0] == (                   'WB_1750_CLIMATE_CHANGE_ADAPTATION_IMPACTS'
                                        )) == True :
                        GKG_['Climate_Change'][i]=True
                       
                        




                    if (split[k][0] == ('WB_1847_CLIMATE_FINANCE'	)) == True :
                        GKG_['Climate_Finance'][i]=True
                         
                    if (split[k][0] == ('WB_1844_MARKET_BASED_CLIMATE_CHANGE_MITIGATION')) == True :
                        GKG_['Climate_Finance'][i]=True
                        
                    if (split[k][0] == ('WB_573_CLIMATE_RISK_MANAGEMENT')) == True :
                        GKG_['Climate_Finance'][i]=True
                        
                    if (split[k][0] == ('WB_1849_PUBLIC_CLIMATE_FINANCE')) == True :
                        GKG_['Climate_Finance'][i]=True
                        
                    if (split[k][0] == ('WB_1850_PRIVATE_CLIMATE_FINANCE')) == True :
                        GKG_['Climate_Finance'][i]=True
                        
                    if (split[k][0] == ('WB_1838_CLIMATE_RISK_SCREENING')) == True :
                        GKG_['Climate_Finance'][i]=True
                        
                    if (split[k][0] == ('WB_582_GREENHOUSE_GAS_ACCOUNTING'
                                          )) == True :
                        GKG_['Climate_Finance'][i]=True
                        


                    if  (split[k][0] == ('ENV_WINDPOWER'))== True: 
                      GKG_['GREEN_ENERGY'][i]=True
                      
                    if  (split[k][0] == ('ENV_SOLAR' ))== True:
                      GKG_['GREEN_ENERGY'][i]=True
                      
                    if  (split[k][0] == ('ENV_HYDRO' ))== True:
                      GKG_['GREEN_ENERGY'][i]=True
                      
                    if  (split[k][0] == ('ENV_BIOFUEL' ))== True:
                      GKG_['GREEN_ENERGY'][i]=True
                      
                    if  (split[k][0] == ('ENV_GEOTHERMAL'))== True:
                      GKG_['GREEN_ENERGY'][i]=True
                      
                    if  (split[k][0] == ('WB_525_RENEWABLE_ENERGY'))== True:
                      GKG_['GREEN_ENERGY'][i]=True
                      
                                          
                        

                        
                    # if (split[k][0] == ('ENV_METALS'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (split[k][0] == ('ENV_MINING'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (split[k][0] == ('ENV_FISHERY'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (split[k][0] == ('ENV_FORESTRY'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (split[k][0] == ('ENV_WATERWAYS'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (split[k][0] == ('WB_566_ENVIRONMENT_AND_NATURAL_RESOURCES'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (split[k][0] == ('WB_897_MINING_ENVIRONMENTAL_MANAGEMENT'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (split[k][0] == ('ENV_DEFORESTATION' ))==True:
                    #     GKG_['NAT_RES'][i]=True
                       
                    # if (split[k][0] == ('ENV_OVERFISH'))==True:
                    #     GKG_['NAT_RES'][i]=True
                       



                    if (split[k][0] == ( 'MANMADE_DISASTER_ENVIRONMENTAL_DISASTER'))==True:
                        GKG_['CRIMEDISASTER'][i]=True
                        
                    if (split[k][0] == ( 'WB_1831_ENVIRONMENTAL_CRIME_AND_LAW_ENFORCEMENT'))==True:
                        GKG_['CRIMEDISASTER'][i]=True
                        
                    if (split[k][0] == ('WB_2916_ENVIRONMENTAL_LAW_ENFORCEMENT'))==True:
                        GKG_['CRIMEDISASTER'][i]=True
                        
                    if (split[k][0] == ('WB_2915_ENVIRONMENTAL_CRIME'))==True:
                        GKG_['CRIMEDISASTER'][i]=True
                       
                    if (split[k][0] == ('MANMADE_DISASTER_MARITIME_ENVIRONMENTAL_DISASTER'))==True:
                        GKG_['CRIMEDISASTER'][i]=True
                        
                    if (split[k][0] == ('SELF_IDENTIFIED_ENVIRON_DISASTER'))==True:
                        GKG_['CRIMEDISASTER'][i]=True
                        
                    if (split[k][0] == ('WB_1936_ENVIRONMENTAL_CRIME_ENFORCEMENT'))==True:
                        GKG_['CRIMEDISASTER'][i]=True
                       
                            
                       


                    if (split[k][0] ==('WB_901_ENVIRONMENTAL_SAFEGUARDS'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_849_ENVIRONMENTAL_LAWS_AND_REGULATIONS'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_1785_ENVIRONMENTAL_POLICIES_AND_INSTITUTION'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'ECON_DEVELOPMENTORGS_UNITED_NATIONS_ENVIRONMENT_PROGRAMME'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_1782_ENVIRONMENTAL_AGREEMENTS_AND_CONVENTIONS'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_1783_ENVIRONMENTAL_GOVERNANCE'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_2307_ENVIRONMENTAL_MANAGEMENT_AND_MITIGATION_PLANS'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_2306_ENVIRONMENTAL_IMPACT_ASSESSEMENT'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_1376_ENVIRONMENTAL_OFFSETS'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_157_ENVIRONMENTAL_WATER_USE_AND_CATCHMENT_PROTECTION'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_1378_PAYMENT_FOR_ENVIRONMENT_SERVICES'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_2195_ENVIROMENTAL_IMPACT_ASSESSMENT'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_598_ENVIRONMENTAL_MANAGEMENT'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_526_RENEWABLE_ENERGY_POLICY_AND_REGULATION'))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_1057_SUSTAINABLE_FOREST_MANAGEMENT'
                            ))== True:
                        GKG_['ENV_POL_MAN'][i]=True
                        
                    if (split[k][0] ==( 'WB_1792_ENVIRONMENTAL_HEALTH'))== True:
                        GKG_['EnvHealth'][i]=True
                        
                    if (split[k][0] ==( 'WB_1717_URBAN_POLLUTION_AND_ENVIRONMENTAL_HEALTH'
                            ))== True:
                        GKG_['EnvHealth'][i]=True
                        
                    if (split[k][0] ==('WB_2197_ENVIRONMENTAL_ENGINEERING'))== True:
                        GKG_['Climate_Science'][i] = True
                        
                    if (split[k][0] ==( 'ENV_CARBONCAPTURE'))== True:
                        GKG_['Climate_Science'][i] = True
                        
                    if (split[k][0] ==( 'WB_571_CLIMATE_SCIENCE'))== True:
                        GKG_['Climate_Science'][i] = True
                        
                    if (split[k][0] ==( 'WB_1784_ENVIRONMENTAL_INFORMATION_MANAGEMENT'))== True:
                        GKG_['Climate_Science'][i] = True
                        
                    if (split[k][0] ==( 'WB_399_INNOVATION_FOR_GREEN_GROWTH'
                            ))== True:
                        GKG_['Climate_Science'][i] = True
                        
                        



                    if (split[k][0] == ( 'WB_476_GREEN_GROWTH'  ))== True:
                        GKG_['Green_Econ'][i] = True          
                                            
                    if (split[k][0] == ( 'WB_2674_GREEN_JOBS'))== True:
                        GKG_['Green_Econ'][i] = True          
                        
                    if (split[k][0] == ('WB_1100_SUSTAINABLE_GROWTH'))== True:
                        GKG_['Green_Econ'][i] = True          
                        
                    if (split[k][0] == ( 'WB_1856_TRADE_AND_THE_ENVIRONMENT'))== True:
                        GKG_['Green_Econ'][i] = True          
                        
                    if (split[k][0] == ( 'WB_791_TRANSPORT_IMPACT_ON_THE_ENVIRONMENT'))== True:
                        GKG_['Green_Econ'][i] = True          
                        
                            


                    if (split[k][0] == ( 'WB_802_GREEN_CITIES'))== True:
                        GKG_['Urban_RE'][i] = True
                        
                    if (split[k][0] == ('WB_408_GREEN_BUILDINGS' ))== True:
                        GKG_['Urban_RE'][i] = True
                        

        GKG_['flag'] = pd.Series([False for x in range(len(GKG_.index))])
        GKG_['flag'] = GKG_['Climate_Change'] + GKG_['Climate_Finance'] 
        + GKG_['GREEN_ENERGY'] + GKG_['NAT_RES'] + GKG_['CRIMEDISASTER'] 
        + GKG_['EnvHealth'] + GKG_['ENV_POL_MAN'] + GKG_['Climate_Science'] 
        + GKG_['Urban_RE']+GKG_['Green_Econ']

        cleanGKG = GKG_[GKG_['flag']>0]
        del cleanGKG['DATE']
        del cleanGKG['COUNTS']
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


print('Primary data cleaning finished')

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
    