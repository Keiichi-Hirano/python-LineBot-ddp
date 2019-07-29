"""
author          : nsuhara <na010210dv@gmail.com>
date created    : 2019/5/1
python version  : 3.7.3
"""
import datetime
import logging

logger = logging.getLogger(__name__)

# DMBS 
DB_answer = ''
RDBMS = 'RDBMS使用の必須要件が発生した場合に、RDBMS(Oracle/DB2/PostgreSQL)を使用\n'
MarkLogic  = 'MarklogicをDataHUBとして使用\n'
Hadoop  = 'Data Aggregation(集計)データの格納を目的にDWHとしてHadoopを使用\n'
HANA  = 'CokeOne Dataをリアルタイムにレポート・分析する際にHANAを使用\n'
CokeOne  = 'CokeOneトランザクションの更新を伴う場合は、CokeOneシステムを使用\n'
# Business Logic
Logic_answer = ''
Abinito = 'ETLに関わるすべての処理を担うプラットフォームとしてAbInitoを使用(複数データの非同期更新）\n'
JAVA = 'API及び、データエントリーに関わるGUIの開発にてJAVA/Java Scriptを使用(少量データの即時同期更新)\n'
Python = '統計解析・分析・シュミレーション処理開発にPython及びRを使用※JAVA代替としも使用可能\n'
ABAP = 'CokeOne・HANAを始めとするSAP環境では、専用開発言語のABAPを使用\n'

# Presentation
Pre_answer = ''
BI_tool = '分析用にAggregation(集計)されたデータを元に' + \
'データを可視化(Visualization)分析を行う際にTableauまたは、Sisenseを使用' + \
'※可視化のパターン変化が多い場合、継続して使用可能\n'
UI5 = 'SAP HANA上でのレポートを行う際にUI5(SAPのHTMLベースGUI)を使用'
HTML5 = 'HTML5：標準化選定にてCokeOne以外のシステムはGUIをHTML5で構築する為' + \
'UIを使用の際はHTML5を使用\n' + \
'D3:Tableauで可視化(Visualization)されたものをHTMLベースで再構築する際に使用' + \
'※可視化のパターン変化が少ない、又は、レポートの代替機能構築時使用\n'
SAP_GUI = 'SAP専用GUIを使用\n'
Export_File = 'UIの構築を伴わない場合、File Exportを実装(AbInito)\n'

class Process(object):
    def __init__(self):
        pass

#    def DDP_check_process(self):
    def DDP_check_process(self,check1,check2,check3,check4,check5):
#       CokeOne Transaction
        if check1 == 'Y':
#           CokeOne read only
            if check2 == 'Y':
#               Realtime
                if check4 == 'Y':
                    DB_answer = HANA
                    Logic_answer = ABAP
#                   Use UI                        
                    if check3 == 'Y':
                        Pre_answer = UI5
                    else:
                        Pre_answer = Export_File                               
#               Non-Realtime
                else:                
                    DB_answer = MarkLogic
                    Logic_answer = Abinito
#                   Use UI                        
                    if check3 == 'Y':
                        Pre_answer = HTML5
#                   Non-Use UI                        
                    else:
                        Pre_answer = Export_File                               
#                   Analytics
                    if check5 == 'Y':
                        DB_answer = DB_answer + 'また' + Hadoop
                        Logic_answer = Logic_answer + 'また' + Python
#                   Non-Analytics
                    else:                
                        pass
#                   Use UI + Analytics
                    if check3 == 'Y' and check5 == 'Y':     
                        Pre_answer = Pre_answer + 'また' + BI_tool
            else:
#           CokeOne CRUD
                DB_answer = CokeOne
                Logic_answer = ABAP
#               Use UI                        
                if check3 == 'Y':
                    Pre_answer = SAP_GUI
#               Non-Use UI                        
                else:
                    Pre_answer = Export_File
#       CokeOne Transaction以外
        else:
            DB_answer = RDBMS + 'また' + MarkLogic
            Logic_answer = Abinito               
#           Use UI
            if check3 == 'Y':
                Pre_answer = HTML5
#           Non-Use UI
            else:
                Pre_answer = Export_File                               
#           Analytics
            if check5 == 'Y':
                DB_answer = DB_answer + 'また' + Hadoop
                Logic_answer = Logic_answer + 'また' + Python
#           Non-Analytics
            else:                
                pass
#           Use UI + Analytics
            if check3 == 'Y' and check5 == 'Y':     
                Pre_answer = Pre_answer + 'また' + BI_tool
#           Realtime
            if check4 == 'Y':
                Logic_answer = Logic_answer + 'また' + JAVA
#        return '1は{}・2は{}・3は{}・4は{}・5は{}です\n'.format(check1,check2,check3,check4,check5)
        return '1.DBは{}\n2.開発言語は{}\n3.プレゼンテーション機能は{}が推奨となります。'.format(DB_answer,Logic_answer,Pre_answer)

#    def _get_week_number(self, date_time):
#        day = date_time.day
#        week_number = 0
#        while day > 0:
#            week_number += 1
#            day -= 7
#        return week_number
