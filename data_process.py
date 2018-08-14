#coding=gbk
import matplotlib.pyplot as plt
import seaborn as sn
import csv
import time
import requests
import pandas
import patsy
import statsmodels.api as sm
import numpy as np

def clean_data():
    data_path = "example.csv"
    raw_path = "info.csv"
    row_list = []
    x = 0
    with open(raw_path,'r') as r:
        rr = csv.reader(r)
        num = 0
        for r_row in rr:
            info_dict = {}
            if num%50 == 0:
                time.sleep(60)
            if len(r_row[-1]) == 0 or len(r_row[0]) == 0 or len(r_row[1]) == 0 or len(r_row[2]) == 0 or r_row[-1] == "square":
                continue
            else:
                info_dict["position"] = r_row[0]
                info_dict["name"] = r_row[1]
                info_dict["price"] = r_row[2]
                info_dict["square"] = r_row[3]
                try:
                    print("正在获取数据...")
                    req = requests.get("https://restapi.amap.com/v3/geocode/geo?key=7a68ede7b7010c772c9ff39ae5b49993&address="+r_row[0]+"&city=太原",timeout=20)
                    info_dict["code"] = req.json()["geocodes"][0]["adcode"]
                    print(info_dict["code"])
                    num += 1
                except:
                    continue
                row_list.append(info_dict.values())

    with open("final.csv",'w',newline='') as a:
        aw = csv.writer(a)
        aw.writerow(info_dict.keys())
        aw.writerows(row_list)

def predict_0():
    df = pandas.read_csv("final.csv",encoding='gbk')
    df2 = df[df.code == 140107]
    df3 = df[df.code == 140105]
    cols = ['square','price','code']
    print(df[df['code'] == 140107])
    # # plt.plot(list(df2[df2.square]),list(df2[df2.price]),'ro')
    # sn.pairplot(df[cols],kind='reg',size=2.5,hue="code")
    # plt.show()
predict_0()
