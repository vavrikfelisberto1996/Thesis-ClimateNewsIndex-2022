import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os 
import datetime

start_date = datetime.date(2015, 3, 19)
end_date = datetime.date(2022, 4, 1)
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
       
        S=pd.Series(GKG_.THEMES)
        GKG_['Climate_Change'] = S.str.contains("WB_567_CLIMATE_CHANGE|ENV_CLIMATECHANGE|UNGP_CLIMATE_CHANGE_ACTION|UNGP_CLIMATE_CHANGE_ACTION|WB_1773_CLIMATE_CHANGE_IMPACTS|WB_574_CLIMATE_CHANGE_ADAPTATION|WB_959_CLIMATE_CHANGE_LAW|WB_747_SOCIAL_RESILIENCE_AND_CLIMATE_CHANGE|WB_1839_OZONE_LAYER_DEPLETION_AND_CLIMATE_CHANGE|WB_575_COMMUNITY_BASED_CLIMATE_ADAPTATION|WB_1750_CLIMATE_CHANGE_ADAPTATION_IMPACTS",regex=True)
        GKG_['Climate_Finance'] = S.str.contains("WB_1847_CLIMATE_FINANCE|WB_1844_MARKET_BASED_CLIMATE_CHANGE_MITIGATION|WB_573_CLIMATE_RISK_MANAGEMENT|WB_1849_PUBLIC_CLIMATE_FINANCE|WB_1850_PRIVATE_CLIMATE_FINANCE|WB_1838_CLIMATE_RISK_SCREENING|WB_582_GREENHOUSE_GAS_ACCOUNTING",regex=True)
        GKG_['GREEN_ENERGY'] = S.str.contains("ENV_WINDPOWER|ENV_SOLAR|ENV_HYDRO|ENV_BIOFUEL|ENV_GEOTHERMAL|WB_525_RENEWABLE_ENERGY",regex=True)
        GKG_['CRIMEDISASTER'] = S.str.contains("MANMADE_DISASTER_ENVIRONMENTAL_DISASTER|WB_1831_ENVIRONMENTAL_CRIME_AND_LAW_ENFORCEMENT|WB_2916_ENVIRONMENTAL_LAW_ENFORCEMENT|WB_2915_ENVIRONMENTAL_CRIME|MANMADE_DISASTER_MARITIME_ENVIRONMENTAL_DISASTER|SELF_IDENTIFIED_ENVIRON_DISASTER|WB_1936_ENVIRONMENTAL_CRIME_ENFORCEMENT|",regex=True)                            
        GKG_['ENV_POL_MAN'] = S.str.contains("WB_901_ENVIRONMENTAL_SAFEGUARDS|WB_849_ENVIRONMENTAL_LAWS_AND_REGULATIONS|WB_1785_ENVIRONMENTAL_POLICIES_AND_INSTITUTION|ECON_DEVELOPMENTORGS_UNITED_NATIONS_ENVIRONMENT_PROGRAMME|WB_1782_ENVIRONMENTAL_AGREEMENTS_AND_CONVENTIONS|WB_1783_ENVIRONMENTAL_GOVERNANCE|WB_2307_ENVIRONMENTAL_MANAGEMENT_AND_MITIGATION_PLANS|WB_2306_ENVIRONMENTAL_IMPACT_ASSESSEMENT|WB_1376_ENVIRONMENTAL_OFFSETS|WB_157_ENVIRONMENTAL_WATER_USE_AND_CATCHMENT_PROTECTION|WB_1378_PAYMENT_FOR_ENVIRONMENT_SERVICES|WB_2195_ENVIROMENTAL_IMPACT_ASSESSMENT|WB_598_ENVIRONMENTAL_MANAGEMENT|WB_526_RENEWABLE_ENERGY_POLICY_AND_REGULATION|WB_1057_SUSTAINABLE_FOREST_MANAGEMENT",regex=True)
        GKG_['Climate_Science'] = S.str.contains("WB_2197_ENVIRONMENTAL_ENGINEERING|ENV_CARBONCAPTURE|WB_571_CLIMATE_SCIENCE|WB_1784_ENVIRONMENTAL_INFORMATION_MANAGEMENT|WB_399_INNOVATION_FOR_GREEN_GROWTH",regex=True) 
        GKG_['Green_Econ']=S.str.contains("WB_476_GREEN_GROWTH|WB_2674_GREEN_JOBS|WB_1100_SUSTAINABLE_GROWTH|WB_1856_TRADE_AND_THE_ENVIRONMENT|WB_791_TRANSPORT_IMPACT_ON_THE_ENVIRONMENT",regex=True)
        
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

