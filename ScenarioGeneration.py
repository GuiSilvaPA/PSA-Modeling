from PowerSystemsAnalysis import *

import shutil, os, glob
from tqdm import tqdm



# for idx in tqdm(range(10000, 20000)):

#     path = f'D:/Modeling/REDE/'

#     if not os.path.exists(path):
#         os.makedirs(path)

#     DG = ScenarioGenerator(net_path='D:/Modeling/BASE/bus68.ntw', dyn_path='D:/Modeling/BASE/bus68.dyn')

#     DG.Sbase(b_min=3, b_max=9, low=0.20, high=0.8)
#     DG.Reforco(b_min=3, b_max=15)
#     DG.RemoveLT(b_min=3, b_max=9)
#     DG.RemoveGen()
#     DG.ChangeLoad(carga='D:/Modeling/BASE/CARGA.csv', min_load=25, max_load=120)

#     DG.Save(net_path=path+f'R{idx:04d}.ntw',
#             dyn_path=path+f'R{idx:04d}.dyn',
#             wfs_path=path+f'R{idx:04d}.dsa',
#             wfs_list=['Organon.prm', f'R{idx:04d}.ntw', f'R{idx:04d}.dyn', 'bus68.evt', 'bus68.plv'])

#     DG.GenerateEvent(path=path+'MOD.evt')

# # 38804

# for idx in tqdm(range(50000, 60000)):

#     path = f'D:/Modeling/REDE/'

#     if not os.path.exists(path):
#         os.makedirs(path)

#     DG = ScenarioGenerator(net_path='D:/Modeling/MOD/bus68.ntw', dyn_path='D:/Modeling/MOD/bus68.dyn')

#     DG.Sbase(b_min=3, b_max=10, low=0.15, high=0.9)
#     DG.Reforco(b_min=3, b_max=15)
#     DG.RemoveLT(b_min=2, b_max=9)
#     DG.RemoveGen()
#     DG.ChangeLoad(carga='D:/Modeling/BASE/CARGA.csv', min_load=10, max_load=120, H=True, FILE='D:/Modeling/BASE/INERCIA.csv')

#     DG.Save(net_path=path+f'R{idx:04d}.ntw',
#         dyn_path=path+f'R{idx:04d}.dyn',
#         wfs_path=path+f'R{idx:04d}.dsa',
#         wfs_list=['Organon.prm', f'R{idx:04d}.ntw', f'R{idx:04d}.dyn', 'bus68.evt', 'bus68.plv'])


#     DG.GenerateEvent(path=path+'MOD.evt')


path_script = 'D:/Modeling/RST_automation.txt'
with open(path_script, 'w') as f:
    for idx in range(55516, 60000):

        f.write(f'Open "D:/Modeling/REDE/R{idx:04d}.dsa"')
        f.write('\n')
        f.write('OPF')
        f.write('\n')
        f.write('DSA DOP')
        f.write('\n')
        f.write(f'Save "D:/Modeling/REDE/R{idx:04d}D.ntw"')
        f.write('\n')
