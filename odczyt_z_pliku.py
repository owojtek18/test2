import pandas as pd
import numpy as np


file = r'C:\Users\wojci\Desktop\test\ICV.txt'
head = ['ac_operation','ac_ticketlabel','country_ID','(was local period)','nc_periodid','(was local shop)','Sirval shop','EAN/PLU','cref suffix','Volumetric, etc','nc_nan','conv factor','nc_slot1','nc_slot2','nc_slot3','nc_slot4','nc_slot5','nc_slot6','nc_slot7','nc_slot8','nc_slot9','nc_slot10','ac_cslot1','ac_cslot2','Comment','Hash Signature']
#dtype={'A': np.int64, 'B': np.float64}
data = pd.read_csv(file, sep=';', header=None, names=head, dtype='str')
data.nc_periodid=data.nc_periodid.astype(int)
#data.info()
#periods=np.linspace(1976,1977,2)
#print(periods)
#print(type(periods))

filter=np.logical_and( data['nc_periodid'] >= 1976, data['nc_periodid'] <= 1977)

new_data=data.loc[filter]

print(new_data.head())
#cref=data['EAN/PLU'].unique()

cref=pd.DataFrame(data['EAN/PLU'].unique())
#print(cref)
cref.to_csv(r'C:\Users\wojci\Desktop\test\ICV_cref.txt',sep=';', header=False, index=False)
