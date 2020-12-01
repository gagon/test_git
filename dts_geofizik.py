import pandas as pd
import sys
import numpy as np
import csv
from matplotlib import pyplot as plt
import os

import lasio

# folder=r"C:\Users\B.Zhumabayev\Desktop\gecko\data_WellA\raw_DTS\orig_809"
folder=r"C:\Users\zhumab\Desktop\sandbox_python-main"
# folder=r"C:\Users\B.Zhumabayev\Desktop\gecko\data_WellA\raw_DTS\test"

df=pd.DataFrame()

i=0
for file in os.listdir(folder):
    if file.endswith(".las"):
        print(file)
        las = lasio.read(os.path.join(folder,file))
        if i==0:
            df=las.df()
        else:
            df=df.join(las.df())
        i+=1

cols=df.columns.tolist()
cols.sort()

# print(cols)
# df=df.sort_index(axis = 1)

# split=int(len(cols)/2)

df=df[cols]

df.to_csv("orig_data.csv",index=False)


#
# for c in df.columns:
#     print(c)

# # print(las.curves)
#
# df = las.df()
#
# print(df.head())
#
# plt.pcolor(df.values[15000:18000,],cmap='jet')
# plt.pcolor(df.values,cmap='jet')
# #
# plt.gca().invert_yaxis()
# #
# plt.show()

# df=pd.read_csv("809_dts.csv")

#
# print(df)
#
# depths=df["Depth"].values
# i=0
# for (columnName, columnData) in df.iteritems():
#
#    if i>0:
#        plt.plot(columnData.values,depths)
#    i+=1
#

# plt.show()




# inFile = File(r'C:\Users\B.Zhumabayev\Desktop\gecko\data_WellA\raw_DTS\orig_809\1.las', mode='r')
#
# I = inFile.Classification == 2
#
# print(I)

#
# timestamps=df["Date"].unique()
#
#
# data=[]
# rows=1000
# columns=3000
#
# depths=[i*41.6666 for i in range(24)]
# new_depths=[i for i in range(rows)]
#
# for t in timestamps:
#     orig_trace=((df[df["Date"]==t]["Temperature"]+10)*4.0).tolist()
#
#     new_trace=np.interp(new_depths,depths,orig_trace)
#
#     data.append(new_trace)
#
# data=(np.array(data).T).tolist()
#
#
#
#
#
# with open("out.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data)

# sys.exit()
