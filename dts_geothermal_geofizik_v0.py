import pandas as pd
import sys
import numpy as np
import csv
from matplotlib import pyplot as plt
import os
import lasio
import datetime


def read_txt(file,type):
    res=[]
    with open(file, newline='') as csvfile:
        s = csv.reader(csvfile, delimiter='\n')
        for row in s:
            if type=="float":
                res.append(float(row[0]))
            elif type=="geothermal":
                r=str(row[0]).split("\t")
                res.append([float(r[0]),float(r[1])])
            else:
                res.append(row[0])
    res=np.array(np.array(res).T).tolist()
    return res


def depth_interp_traces(trace,depths):
    temps=np.interp(depths,trace[0],trace[1]).tolist()
    new_trace=[depths,temps]
    return new_trace


def dts_subs_geothermal(dts,geothermal_trace):
    new_dts=np.array((np.array(dts).T-np.array(geothermal_trace)).T).tolist()
    return new_dts



dts_folder=r"C:\Users\zhumab\Desktop\dfo\data\dts_waterfall\flow"
well_geothermal_fullpath=r"C:\Users\zhumab\Desktop\dfo\data\dts_geothermal\geothermal.txt"



df = pd.read_csv(os.path.join(dts_folder,"dts.csv"),header=None)
df = df.replace({np.nan: 0})
dts_data=df.values.tolist()


depths=read_txt(os.path.join(dts_folder,"depths.txt"),"float")

geothermal=read_txt(well_geothermal_fullpath,"geothermal")


new_geothermal=depth_interp_traces(geothermal,depths)
print(new_geothermal)


dts_data=dts_subs_geothermal(dts_data,new_geothermal[1])

new_df=pd.DataFrame(dts_data)

new_df.to_csv("dts_geo.csv",index=False,header=False)
