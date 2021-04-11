from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import sqlite3
import pandas as pd
import json


def check(request):
    data = {
        'hello': 'world',
    }
    print(data)
    return JsonResponse(data)


def allrecords(request):
    con = sqlite3.connect('./tkph.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute(
        "create table if not exists items (date_stamp TEXT primary key not null, date TEXT,customer TEXT,project TEXT, state TEXT,district TEXT,siteAddress TEXT,otherDetails TEXT,tyre_size TEXT,max_amb_temp TEXT,cycle_length TEXT,cycle_duration TEXT,vehicle_make TEXT,vehicle_model TEXT,empty_vehicle_weight TEXT,pay_load TEXT,weight_correction TEXT,load_dist_front_unloaded TEXT,load_dist_rear_unloaded TEXT,load_dist_front_loaded TEXT,load_dist_rear_loaded TEXT,added_by TEXT,distance_km_per_hour TEXT,gross_vehicle_weight TEXT,k1_dist_coefficient TEXT,k2_temp_coefficient TEXT,avg_tyre_load_front TEXT,avg_tyre_load_rear TEXT,basic_site_tkph_front TEXT,basic_site_tkph_rear TEXT,real_site_tkph_front TEXT,real_site_tkph_rear TEXT, uploaded BOOL);")

    values = [1614614604236, "2021-03-01T16:03:24.222Z", "", "", "", "", "", "", "18.00-33", "", 8, "", "CAT", "773B", 39396, 53977.5, "",
              47.3, 52.7, 33.300000000000004, 66.7, "saurabh", "null", 93373.5, 1.09, "null", 12431.920875,
              10380.227062500002, "null", "null", "null", "null", "null"];

    cursorObj.execute('insert into items ("date_stamp","date","customer","project", "state", "district", "siteAddress", "otherDetails", "tyre_size","max_amb_temp","cycle_length","cycle_duration","vehicle_make","vehicle_model","empty_vehicle_weight","pay_load","weight_correction","load_dist_front_unloaded","load_dist_rear_unloaded","load_dist_front_loaded","load_dist_rear_loaded","added_by","distance_km_per_hour","gross_vehicle_weight","k1_dist_coefficient","k2_temp_coefficient","avg_tyre_load_front","avg_tyre_load_rear","basic_site_tkph_front","basic_site_tkph_rear","real_site_tkph_front","real_site_tkph_rear","uploaded") values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',values)

    cursorObj.execute("select * from items;")
    rows = cursorObj.fetchall()
    rs = pd.DataFrame(data=rows,
                      columns=["date_stamp", "date", "customer","project", "state", "district", "siteAddress", "otherDetails", "tyre_size", "max_amb_temp", "cycle_length",
                               "cycle_duration", "vehicle_make", "vehicle_model", "empty_vehicle_weight", "pay_load",
                               "weight_correction", "load_dist_front_unloaded", "load_dist_rear_unloaded",
                               "load_dist_front_loaded", "load_dist_rear_loaded", "added_by", "distance_km_per_hour",
                               "gross_vehicle_weight", "k1_dist_coefficient", "k2_temp_coefficient",
                               "avg_tyre_load_front", "avg_tyre_load_rear", "basic_site_tkph_front",
                               "basic_site_tkph_rear", "real_site_tkph_front", "real_site_tkph_rear", "uploaded"
                               ])
    print(rs)

    js = rs.to_json()
    ps = json.loads(js)

    data = {
        'hello': request.GET.get('q', ''),
    }
    print(data)

    return JsonResponse(ps)


def insertrecords(request):
    print('insert record')
    data = JSONParser().parse(request)

    print(data['date_stamp'])
    con = sqlite3.connect('./tkph.sqlite')

    cursorObj = con.cursor()
    cursorObj.execute(
        "create table if not exists items (date_stamp TEXT primary key not null, date TEXT,customer TEXT,project TEXT, state TEXT,district TEXT,siteAddress TEXT,otherDetails TEXT,tyre_size TEXT,max_amb_temp TEXT,cycle_length TEXT,cycle_duration TEXT,vehicle_make TEXT,vehicle_model TEXT,empty_vehicle_weight TEXT,pay_load TEXT,weight_correction TEXT,load_dist_front_unloaded TEXT,load_dist_rear_unloaded TEXT,load_dist_front_loaded TEXT,load_dist_rear_loaded TEXT,added_by TEXT,distance_km_per_hour TEXT,gross_vehicle_weight TEXT,k1_dist_coefficient TEXT,k2_temp_coefficient TEXT,avg_tyre_load_front TEXT,avg_tyre_load_rear TEXT,basic_site_tkph_front TEXT,basic_site_tkph_rear TEXT,real_site_tkph_front TEXT,real_site_tkph_rear TEXT, uploaded BOOL);")

    values = list(data.values())

    cursorObj.execute(
        'insert into items ("date_stamp","date","customer","project", "state", "district", "siteAddress", "otherDetails","tyre_size","max_amb_temp","cycle_length","cycle_duration","vehicle_make","vehicle_model","empty_vehicle_weight","pay_load","weight_correction","load_dist_front_unloaded","load_dist_rear_unloaded","load_dist_front_loaded","load_dist_rear_loaded","added_by","distance_km_per_hour","gross_vehicle_weight","k1_dist_coefficient","k2_temp_coefficient","avg_tyre_load_front","avg_tyre_load_rear","basic_site_tkph_front","basic_site_tkph_rear","real_site_tkph_front","real_site_tkph_rear","uploaded") values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        values)

    con.commit()

    cursorObj.execute("select * from items;")
    rows = cursorObj.fetchall()
    rs = pd.DataFrame(data=rows,
                      columns=["date_stamp", "date", "customer", "project", "state", "district", "siteAddress", "otherDetails", "tyre_size", "max_amb_temp", "cycle_length",
                               "cycle_duration", "vehicle_make", "vehicle_model", "empty_vehicle_weight", "pay_load",
                               "weight_correction", "load_dist_front_unloaded", "load_dist_rear_unloaded",
                               "load_dist_front_loaded", "load_dist_rear_loaded", "added_by", "distance_km_per_hour",
                               "gross_vehicle_weight", "k1_dist_coefficient", "k2_temp_coefficient",
                               "avg_tyre_load_front", "avg_tyre_load_rear", "basic_site_tkph_front",
                               "basic_site_tkph_rear", "real_site_tkph_front", "real_site_tkph_rear", "uploaded"
                               ])
    print(rs)

    js = rs.to_json()
    ps = json.loads(js)

    data = {
        'hello': ps,
    }
    print(data)

    return JsonResponse(ps)