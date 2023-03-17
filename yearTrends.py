### Ryan Chaban, 03/17/2023

### This file is used to plot the year over year trends in the important questions from the surveys
### Example: would you reccomend?

# takes the list of dataframes from generate_df

import pickle
import matplotlib.pyplot as plt

save_fn = '/home/chabanr/Gdrive/Conferences/APS/StudentDayAnalysis/dflist.pkl'

with open(save_fn, 'rb') as ff:
    dfl = pickle.load(ff)

# plot a pie chart of responses
f, ax = plt.subplots(ncols=3, figsize=(12, 5))
ax = ax.flatten()
for ii in range(len(dfl)):
    dfl[ii]['journey'].value_counts().plot.pie(subplots=True, ax=ax[ii], legend=True)

plt.show()