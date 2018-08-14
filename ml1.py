#coding=gbk
import csv
import requests
import time

def get_pos():
    with open("info.csv",encoding="utf-8") as r:
        rd = csv.reader(r)
        info_list = []
        t = 0
        for row in rd:
            raw_list = []
            if t%50 == 0:
                print("��Ϣ...")
                time.sleep(20)
            t += 1
            if len(row) != 0:
                if row[0] == "":
                    continue
                addr = row[0]
                with open("data.csv",'w',encoding="gbk") as w:
                    url = "https://restapi.amap.com/v3/geocode/geo?address="+addr+"&output=json&key=7a68ede7b7010c772c9ff39ae5b49993"
                    try:
                        r = requests.get(url,timeout=20)
                    except:
                        continue
                    try:
                        print("���ڻ�ȡ��γ��...")
                        raw_list.append(row[0])
                        print(row[0])
                        raw_list.append(r.json()['geocodes'][0]["location"])
                        print(r.json()['geocodes'][0]["location"])
                        info_list.append(raw_list)
                    except:
                        print("except???")
                        continue

        with open('output.csv', 'a', newline='',encoding="gbk") as f:
            writer = csv.writer(f)
            print("����д���ļ�...")
            for row in info_list:
                writer.writerow(row)
