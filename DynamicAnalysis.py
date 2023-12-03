from PowerSystemsAnalysis import *

import os, glob, shutil

from tqdm import tqdm
import pandas as pd

pd.set_option('mode.chained_assignment', None)


# ### ==================================================================================================================================== ###
# ''' EXTRACT: RST's INFO'''
# ### ==================================================================================================================================== ###


PATH    = f'D:/Modeling/REDE/' 
FILES = [PATH + f for f in os.listdir(PATH) if 'rst' in f]
vars  = pd.DataFrame()

for RST in tqdm(FILES):

    RR = RST_Reader(RST)
    a, net_info = RR.generate_json()

    rede = np.expand_dims(np.array(net_info).ravel(), axis=(0))
    columns = []
    for isl in net_info['ISLD']:
        for col in net_info.columns:
            columns.append(col + '_I' + isl)
    net_info = pd.DataFrame(rede, columns=columns)

    name          = RST.split('/')[-1].split('.')[0]
    RP            = RST_Process(a, name=name)
    RP.df.columns = [col[0] if col[1] == '' else col[0] + '_' + col[1] for col in RP.df.columns]

    RP.df['Contigence'] = [int(a.split('_')[-1]) for a in RP.df['Contigence']]
    RP.df['OP']         = name
    RP.df['A_CODE']     = RP.df['A_CODE'].astype('int')

    RP.df = RP.df.sort_values(by=['OP', 'Contigence']).reset_index(drop=True)
    
    net_info['OP'] = RP.df['OP'].values[0]

    RP.df = RP.df.merge(net_info, on='OP', how='left')

    # print(RP.df)
    # print(vars)

    vars  = pd.concat([vars, RP.df]).reset_index(drop=True)

vars.to_csv(PATH.replace('OUT/', '') + 'vars.csv', index=False)

print(vars)




