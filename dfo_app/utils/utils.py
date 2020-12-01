import json
import os
import csv
import datetime
import numpy as np

# required for saving json files
dirname=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')) # added after restructuring files/folders

def get_session_json():
    json_fullpath=os.path.join(dirname,r"temp\session.json")
    if os.path.isfile(json_fullpath):
        data = json.load(open(json_fullpath))
    else:
        data={}
    return data


def save_session_json(session):
    json_fullpath=os.path.join(dirname,r"temp\session.json")
    json.dump(session, open(json_fullpath, 'w'),indent=4, sort_keys=True)
    return "None"


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


def read_pt(file):
    res=[]
    with open(file, newline='') as csvfile:
        s = csv.reader(csvfile, delimiter='\n')
        for row in s:
            r=str(row[0]).split("\t")
            # print(r)
            # t=datetime.datetime.strptime(r[0],"%m/%d/%Y %I:%M")
            # t=t.strftime("%Y-%m-%d %H:%M:%S")
            res.append([r[0],float(r[1]),float(r[2])])
    res=np.array(np.array(res).T).tolist()
    return res

def convert_timestamps(timestamps,format1,format2,dhour):
    t_new=[]
    for t in timestamps:
        if dhour>=0:
            t=datetime.datetime.strptime(t,format1)+datetime.timedelta(hours=abs(dhour))
        else:
            t=datetime.datetime.strptime(t,format1)-datetime.timedelta(hours=abs(dhour))
        t_new.append(t.strftime(format2))
    return t_new


def depth_interp_traces(trace,depths):
    temps=np.interp(depths,trace[0],trace[1]).tolist()
    new_trace=[depths,temps]
    return new_trace


def dts_subs_geothermal(dts,geothermal_trace):
    new_dts=np.array((np.array(dts).T-np.array(geothermal_trace)).T).tolist()
    return new_dts
