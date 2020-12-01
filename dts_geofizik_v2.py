import pandas as pd
import sys
import numpy as np
import csv
from matplotlib import pyplot as plt
import os
import lasio
import datetime

# folder=r"C:\Users\B.Zhumabayev\Desktop\gecko\data_WellA\raw_DTS\orig_809"
# folder=r"C:\Users\zhumab\Desktop\sandbox_python-main\static"
folder=r"C:\Users\zhumab\Desktop\sandbox_python-main\flow"
# folder=r"C:\Users\B.Zhumabayev\Desktop\gecko\data_WellA\raw_DTS\test"

# df=pd.DataFrame()
#
# i=0
# for file in os.listdir(folder):
#     if file.endswith(".las"):
#         print(file)
#         las = lasio.read(os.path.join(folder,file))
#         if i==0:
#             df=las.df()
#         else:
#             df=df.join(las.df())
#         i+=1
#
# cols=df.columns.tolist()
# depths=list(df.index.values)
# cols.sort()
#
# print(cols)
# # df=df.sort_index(axis = 1)
#
# # split=int(len(cols)/2)
#
# df=df[cols]

# df.to_csv("orig_data_flow.csv",index=False,header=False)
# df.to_csv("orig_data_static.csv",index=False,header=False)


# with open('timestamps_static.txt', 'w') as f:
#     for item in cols:
#         f.write("%s\n" % item)

# with open('depths_flow.txt', 'w') as f:
#     for item in depths:
#         f.write("%s\n" % item)




df=pd.read_csv("orig_data_static.csv",header=None)

depth=[]
with open('depths_static.txt', newline='') as csvfile:
    s = csv.reader(csvfile, delimiter='\n')
    for row in s:
        depth.append(float(row[0]))

timestamps=[]
with open('timestamps_static.txt', newline='') as csvfile:
    s = csv.reader(csvfile, delimiter='\n')
    for row in s:
        timestamps.append(row[0])
#

# df=pd.read_csv("orig_data_flow.csv",header=None)
#
# depth=[]
# with open('depths_flow.txt', newline='') as csvfile:
#     s = csv.reader(csvfile, delimiter='\n')
#     for row in s:
#         depth.append(float(row[0]))
#
# timestamps=[]
# with open('timestamps_flow.txt', newline='') as csvfile:
#     s = csv.reader(csvfile, delimiter='\n')
#     for row in s:
#         timestamps.append(row[0])


tol=0.1

print(df.head())

new_df=pd.DataFrame()
new_timestamps=[]


for i in range(len(timestamps)-1):
    curr_time=datetime.datetime.strptime(str(timestamps[i]),"%Y-%m-%dT%H_%M_%S")
    next_time=datetime.datetime.strptime(str(timestamps[i+1]),"%Y-%m-%dT%H_%M_%S")

    curr_trace=list(df[i].values)

    new_df[timestamps[i]]=curr_trace
    new_timestamps.append(timestamps[i])

    dt_traces=(next_time-curr_time).total_seconds()

    if i==0:
        dt=dt_traces
        trace_len=len(curr_trace)

    if dt_traces>dt*(1.0+tol):

        new_time=curr_time

        while new_time+datetime.timedelta(seconds=dt)<next_time:

            new_time+=datetime.timedelta(seconds=dt)

            new_time_str=new_time.strftime("%Y-%m-%dT%H_%M_%S")
            new_df[new_time_str]=np.zeros(trace_len)
            new_timestamps.append(new_time_str)

            # trace_idx=time_collection.index(time_collection[i])

print(new_df.shape)

# new_df.to_csv("new_data_flow.csv",index=False,header=False)
new_df.to_csv("new_data_static.csv",index=False,header=False)

# with open('new_timestamps_flow.txt', 'w') as f:
#     for item in new_timestamps:
#         f.write("%s\n" % item)


with open('new_timestamps_static.txt', 'w') as f:
    for item in new_timestamps:
        f.write("%s\n" % item)


# df=pd.read_csv("new_data_flow.csv",header=None)
df=pd.read_csv("new_data_static.csv",header=None)

vmin=18
vmax=50

extent=[new_timestamps[1],new_timestamps[-1],depth[-1],depth[0]]

plt.imshow(df.values,cmap='jet',aspect='auto',interpolation='none',vmin=vmin,vmax=vmax)
plt.colorbar()
plt.show()
