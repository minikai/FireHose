import requests
import json
import pandas as pd
import configparser
import csv
import datetime
import numpy as np
import time

config = configparser.ConfigParser()
config.read('ex_config.ini')
duration_API = config['push_data']['duration_API']
url = config['api']['url']



df1 = pd.read_csv('testing_data.txt', header=None)


a = df1.shape[0]
b = df1.shape[1]


def instructions_data_structure(timeslice_str):
    arr = timeslice_str.split(';')
    if len(arr) != 14:
        return timeslice_str
    else:
        instructions = {}
        instructions['STATUS_EQUIPMENT']=int(arr[0])
        instructions['STATUS_FAN']=int(arr[1])
        instructions['VOLTAGE_INPUT']=float(arr[2])
        instructions['CURRENT_INPUT']=float(arr[3])
        instructions['PRESSURE_OUTPUT']=float(arr[4])
        instructions['TEMPERATURE_OUTPUT']=int(arr[5])
        instructions['KW_FAN']=float(arr[6])
        instructions['KW_EQUIPMENT']=float(arr[7])
        instructions['FREQ_FAN']=float(arr[8])
        instructions['KW_SUMMARY']=float(arr[9])
        instructions['PRESSURE_EQUIPMENT']=float(arr[10])
        instructions['TEMPERATURE_EQUIPMENT']=int(arr[11])
        instructions['TEMPERATURE_ENVIRONMENT']=float(arr[12])
        return instructions
c = 0
d = []

for i in range(a):
    for ii in range(0, b - 2):
        if c != 10 :
            if type(df1[df1.columns[ii]][i]) == float or type(df1[df1.columns[ii]][i]) == np.float64:
                pass
            else:
                fields = {}
                fields = instructions_data_structure(df1[df1.columns[ii]][i])
                d.append(fields)
                c = c + 1
        else :
            e = {}
            e['data']=d
            r = requests.post(url, json=e)
            time.sleep(int(duration_API))
            c = 0
            #print e
            print (e)
            d = []
#print "end"
print ("end")