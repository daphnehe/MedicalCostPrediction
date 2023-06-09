# -*- coding: utf-8 -*-

import pandas as pd
pd.read_csv('/content/drive/My Drive/nebula/project_data/medical_cost.csv')
file_path='/content/drive/My Drive/nebula/project_data/medical_cost.csv'
mc_data=pd.read_csv(file_path)
mc_data

from google.colab import drive
drive.mount('/content/drive')

mc_data.head(10)

len(mc_data)

mc_data.describe()

filter_mc_data=mc_data.loc[:,'charges']<50000
clean_mc_data=mc_data.loc[filter_mc_data,:]
clean_mc_data.describe()

clean_mc_data_new=clean_mc_data.loc[filter_mc_data,:]
clean_mc_data_new.describe()

mc_data.groupby('bmi')['charges'].mean()

# years=mc_data.loc[:,'charges'].unique()
# for each_age in years:
#   filter_mc_data=mc_data.loc[:,'charges']==each_age
#   print(f'{each_age} has {len(mc_data.loc[filter_mc_data,:])} record')

# filter_mc_data=mc_data.loc[:,'charges']>1000
# filter_mc_data=mc_data.loc[:,'charges']>55000
# clean_mc_data=mc_data.loc[filter_mc_data,:]
# clean_mc_data.describe()

from scipy.stats import linregress
clean_mc_data.loc[:,['bmi','charges']].plot(kind='scatter',x='bmi',y='charges')

import matplotlib.pyplot as plt

m, b, r, p, std=linregress(clean_mc_data['bmi'],clean_mc_data['charges'])
y_predict=m*clean_mc_data['bmi']+b
mc_data.loc[:,['bmi','charges']].plot(kind='scatter',x='bmi',y='charges')
plt.plot(clean_mc_data['bmi'],y_predict,c='red')
plt.show()

clean_mc_data.loc[:,['bmi','charges']].plot(kind='hist',x='bmi',y='charges')

bmi_charges_pvt=clean_mc_data.loc[:,['bmi','charges']].pivot_table(index='bmi',values='charges',aggfunc='median')
bmi_charges_pvt.plot(kind='line', stacked=True)
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

fig, ax=plt.subplots(1,1,figsize=(10,10))
clean_mc_data.loc[:,['smoker','charges']].boxplot(by='smoker',showfliers=False,rot=90,ax=ax)

mc_by_smoker=clean_mc_data.loc[:,['charges','smoker']].groupby('smoker').median()#median or mean?
mc_by_smoker.plot(kind='bar')
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

mc_by_sex=clean_mc_data.loc[:,['charges','sex']].groupby('sex').median()#median or mean? mean: male higher, median: rel same
mc_by_sex.plot(kind='bar')
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

age_charges_pvt=clean_mc_data.loc[:,['age','charges']].pivot_table(index='age',values='charges',aggfunc='median')#mean or median?
age_charges_pvt.plot(kind='line', stacked=True)
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

mc_by_region=clean_mc_data.loc[:,['charges','region']].groupby('region').median().sort_values('charges',ascending=False)#median or mean? med: ne highest, mean: se highest
mc_by_region.plot(kind='bar')
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

fig, ax=plt.subplots(1,1,figsize=(10,10))
clean_mc_data.loc[:,['region','charges']].boxplot(by='region',showfliers=False,rot=90,ax=ax)

age_region_mc_pvt=clean_mc_data.loc[:,['age','region','charges']].pivot_table(index='age',values='charges',columns='region',aggfunc='median')
age_region_mc_pvt.plot(kind='line', stacked=True)
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

age_sex_mc_pvt=clean_mc_data.loc[:,['age','sex','charges']].pivot_table(index='age',values='charges',columns='sex',aggfunc='median')
age_sex_mc_pvt.plot(kind='line', stacked=False)
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

# children_region_mc_pvt=clean_mc_data.loc[:,['children','region','charges']].pivot_table(index='children',values='charges',columns='region',aggfunc='median')
# children_region_mc_pvt.plot(kind='line', stacked=True)
# plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

children_region_pvt=clean_mc_data.loc[:,['children','region','charges']].pivot_table(index='children',values='charges',columns='region',aggfunc='median')
children_region_pvt.plot(kind='bar', stacked=True)
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

smoker_age_pvt=clean_mc_data.loc[:,['age','smoker','charges']].pivot_table(index='age',values='charges',columns='smoker',aggfunc='count')
smoker_age_pvt.plot(kind='bar', stacked=True)
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))
fig, ax=plt.subplots(1,1,figsize=(10,10))
clean_mc_data.loc[:,['age','charges','smoker']].boxplot(by='age',showfliers=False,rot=90,ax=ax)

age_sex_mc_pvt=clean_mc_data.loc[:,['age','sex','charges']].pivot_table(index='age',values='charges',columns='sex',aggfunc='median')
age_children_mc_pvt.plot(kind='bar', stacked=True)
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))

children_smoker_pvt=clean_mc_data.loc[:,['children','smoker','charges']].pivot_table(index='children',values='charges',columns='smoker',aggfunc='median')
children_age_pvt.plot(kind='bar', stacked=True)
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))
