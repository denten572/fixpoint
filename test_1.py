# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import csv

#障害発生時log
incident_log = ""
#incident_flg = False

with open ( "test_1.csv" , "r" ) as f :
    reader = csv . reader ( f )
    #IPと時間でソート
    sorted_csv = sorted(reader, key=lambda x:(x[1], x[0]))
    for line in sorted_csv :
        #タイムアウトかつインシデントlogが空の場合
        if line[2] == "-" and incident_log == "":
            incident_log = line
        #正常(タイムアウトなし)かつインシデントのIPと処理行のIPが一致する場合
        elif (line[2] != "-" 
              and incident_log != ""
              and line[1] == incident_log[1]):
            print (line[1] + "の故障時間は" + incident_log[0] + "～" + line[0])
            incident_log = ""
        ##インシデントlogが空ではないかつインシデントのIPと処理行のIPが一致しない場合
        elif (incident_log != ""
              and line[1] != incident_log[1]):
            incident_log = ""