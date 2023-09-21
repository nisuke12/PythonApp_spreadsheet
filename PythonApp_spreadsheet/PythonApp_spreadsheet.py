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

# �R�}���h���C�������̎擾
arguments = sys.argv

# �����̐������������m�F
if len(arguments) < 4:
    print("�������s�����Ă��܂�")
    sys.exit(1)

# 
# �����̒l���擾

# CSV�o�̓p�X
# ������
seasoning_csv_file_path = arguments[1]

# �H��
food_csv_file_path = arguments[2]

#���p�i
daily_csv_file_path = arguments[3]



# �������F�t�@�C���쐬
e_cell_values = []  # ��̃��X�g���쐬

d_values = worksheet.range('D3:D99')
e_values = worksheet.range('E3:E99')

for d_cell, e_cell in zip(d_values, e_values):
    if d_cell.value.lower() == "true":
     e_cell_values.append([e_cell.value])  # e_cell�̒l�����X�g�ɒǉ�

     # �o�̓t�@�C�����J��
with open(seasoning_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # �f�[�^����������
    for row in e_cell_values:
        writer.writerow(row)



# �H�ށF�t�@�C���쐬
i_cell_values = []  # ��̃��X�g���쐬

h_values = worksheet.range('H3:H99')
i_values = worksheet.range('I3:I99')

for h_cell, i_cell in zip(h_values, i_values):
    if h_cell.value.lower() == "true":
       i_cell_values.append([i_cell.value])

    # �o�̓t�@�C�����J��
with open(food_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # �f�[�^����������
    for row in i_cell_values:
        writer.writerow(row)




# ���p�i�F�t�@�C���쐬
m_cell_values = []  # ��̃��X�g���쐬

l_values = worksheet.range('L3:L99')
m_values = worksheet.range('M3:M99')

for l_cell, m_cell in zip(l_values, m_values):
    if l_cell.value.lower() == "true":
        m_cell_values.append([m_cell.value])

    # �o�̓t�@�C�����J��
with open(daily_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # �f�[�^����������
    for row in m_cell_values:
      writer.writerow(row)
