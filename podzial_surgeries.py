import glob
import pandas as pd
import os
files = glob.glob(r'C:\Users\wojci\Desktop\korekta\CRF*.txt')
period = int(input('Production_period: '))
for file in files:
    data = pd.read_csv(file, sep=';', header=None, dtype='str')
    print(data[4].head())
    data[4] = data[4].astype('int')

    if data.iat[0, 0] == 'IC':
        if data.iat[0, 9] == 'VOL_RCC':
            data[1] = 'ICV'
        else:
            data[1] = 'ICC'
    elif data.iat[0, 0] == 'DR':
        if data.iat[0, 9] == 'VOL_RCC':
            data[1] = 'DRV'
        else:
            data[1] = 'DRC'
    datan = data[(data[4] > period-13)]
    datao = data[(data[4] < period-12)]
    dir_name = os.path.dirname(file)
    file_name = os.path.basename(file)
    datan.to_csv(dir_name + '\RUN_' + file_name, sep=';', header=False, index=False)
    datao.to_csv(dir_name + '\SEND_' + file_name, sep=';', header=False, index=False)



