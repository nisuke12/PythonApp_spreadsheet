# -*- coding: cp932 -*-


import gspread
import csv
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('C://Users//work0//source//repos//PythonApp_spreadsheet//PythonApp_spreadsheet//pythonspreadsheet-389814-5331db0d9053.json', scope)
gc = gspread.authorize(credentials)
worksheet = gc.open('python_SpreadSheet').sheet1

import sys

# コマンドライン引数の取得
arguments = sys.argv

# 引数の数が正しいか確認
if len(arguments) < 4:
    print("引数が不足しています")
    sys.exit(1)

# 
# 引数の値を取得

# CSV出力パス
# 調味料
seasoning_csv_file_path = arguments[1]

# 食材
food_csv_file_path = arguments[2]

#日用品
daily_csv_file_path = arguments[3]



# 調味料：ファイル作成
e_cell_values = []  # 空のリストを作成

d_values = worksheet.range('D3:D99')
e_values = worksheet.range('E3:E99')

for d_cell, e_cell in zip(d_values, e_values):
    if d_cell.value.lower() == "true":
     e_cell_values.append([e_cell.value])  # e_cellの値をリストに追加

     # 出力ファイルを開く
with open(seasoning_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # データを書き込む
    for row in e_cell_values:
        writer.writerow(row)



# 食材：ファイル作成
i_cell_values = []  # 空のリストを作成

h_values = worksheet.range('H3:H99')
i_values = worksheet.range('I3:I99')

for h_cell, i_cell in zip(h_values, i_values):
    if h_cell.value.lower() == "true":
       i_cell_values.append([i_cell.value])

    # 出力ファイルを開く
with open(food_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # データを書き込む
    for row in i_cell_values:
        writer.writerow(row)




# 日用品：ファイル作成
m_cell_values = []  # 空のリストを作成

l_values = worksheet.range('L3:L99')
m_values = worksheet.range('M3:M99')

for l_cell, m_cell in zip(l_values, m_values):
    if l_cell.value.lower() == "true":
        m_cell_values.append([m_cell.value])

    # 出力ファイルを開く
with open(daily_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # データを書き込む
    for row in m_cell_values:
      writer.writerow(row)
