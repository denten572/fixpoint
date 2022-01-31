# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import csv

def check(number):
    #障害発生時log
    incident_log = ""
    #小以外発生カウント
    incident_count = 0
    
    with open ( "test.csv" , "r" ) as f :
        reader = csv . reader ( f )
        sorted_csv = sorted(reader, key=lambda x:(x[1], x[0]))
        for line in sorted_csv :
            #タイムアウトの場合
            if line[2] == "-":
                incident_count += 1
                #インシデントlogが空の場合
                if incident_log == "":
                    incident_log = line 
            #正常(タイムアウトなし)かつインシデントのIPと処理行のIPが一致する場合
            elif (line[2] != "-" 
                  and incident_log != ""
                  and line[1] == incident_log[1]
                  and incident_count >= number):
                print (line[1] + "の故障時間は" + incident_log[0] + "～" + line[0])
                incident_log = ""
                incident_count = 0
            ##インシデントlogが空ではないかつインシデントのIPと処理行のIPが一致しない場合
            elif (incident_log != ""
                  and line[1] != incident_log[1]):
                incident_log = ""
                incident_count = 0

check(3)
