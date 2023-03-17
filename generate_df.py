### Ryan Chaban, 03/17/2023
## This file is used to agglomerate the SD feedback from csv files
## into a useable pandas df

import pandas as pd
from collections import OrderedDict

import pickle

feedback_directory = '/home/chabanr/Gdrive/Conferences/APS/StudentDayAnalysis/'
base_filename = 'SDfeedback'

save_fn = '/home/chabanr/Gdrive/Conferences/APS/StudentDayAnalysis/dflist.pkl'

# the original dataframes stored with their year as the key
ogdf = OrderedDict()

years = [2019, 2021, 2022]

for year in years:
    ogdf[year] = pd.read_csv(f'{feedback_directory}{base_filename}_{str(year)}.csv')

### The useful columns
### Reccomend?
# 2019 column index 1
# 2021 column index 30
# 2022 column index 35
# these become:
recommend_indx = {2019: 1, 2021: 30, 2022: 35}
# Where are you in your student Journey?
journey_indx = {2019: 11, 2021: 35, 2022: 3}

# put all the column names in here in order and the corresponding dictionary
col_names = ['reccomend', 'journey']
col_indx_maps = [recommend_indx, journey_indx]


# create a list of dataframes that are "filtered" to only have useful things
dfl = []

for ii, year in enumerate(years):
    dfl.append(pd.DataFrame())
    for col_name, indx_key in zip(col_names, col_indx_maps):
        dfl[ii][col_name] = ogdf[year].iloc[:, indx_key[year]]

    print(dfl[ii].describe())


### Save it all to a pickle file
with open(save_fn, 'wb') as ff:
    pickle.dump(dfl, ff)

print(f"Saved dfl to: {save_fn}")



