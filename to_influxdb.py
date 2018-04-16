# -*-coding:utf-8 -*-
from datetime import datetime, timedelta
import json
import csv
import requests
import pandas as pd
from influxdb import InfluxDBClient
import numpy as np
import configparser
import time

# read config file
config = configparser.ConfigParser()
config.read('ex_config.ini')
host = config['influxdb']['host']
port = config['influxdb']['port']
database = config['influxdb']['database']
username = config['influxdb']['username']
password = config['influxdb']['password']
measurement = config['influxdb']['measurement']
duration_IDB = config['push_data']['duration_IDB']


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


client = InfluxDBClient(host, port, username, password, database)  # connect influxdb
df1 = pd.read_csv('training_data.txt', header=None)

data = {}
a = df1.shape[0]  # 資料筆數
b = df1.shape[1]  # 資料欄位
for i in range(a):
    data['measurement'] = measurement
    tags = {}
    tags['sn'] = 'system_data'
    data['tags'] = tags
    for ii in range(0, b - 2):
        fields = {}
        if type(df1[df1.columns[ii]][i]) == float or type(df1[df1.columns[ii]][i]) == np.float64:
            pass
        else:
            fields = instructions_data_structure(df1[df1.columns[ii]][i])
            data['fields'] = fields
            json_body = []
            json_body.append(data)
            #print json_body
            print (json_body)
            client.write_points(json_body)
            time.sleep(int(duration_IDB))
#print "end"
print ("end")
