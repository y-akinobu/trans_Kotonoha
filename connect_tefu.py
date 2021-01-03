import os
import sys
sys.path.append('..')
import collect_aoj
import kotonoha

l_userId = ['tefu417']
l_problemId = [
  'ITP1_1_A', 
  'ITP1_1_B', 
  '0335', 
  '0380', 
  '0315', 
  'ITP1_1_C', 
  'ITP1_2_A', 
  'ITP1_2_B', 
  '0357', 
  '0381', 

  '0257', 
  'ITP1_1_D', 
  'ITP1_4_A', 
  'ITP1_4_B', 
  '0094', 
  'ITP1_2_C', 
  'ITP1_2_D', 
  '0345', 
  '0641', 
  '0652', 

  'ITP1_3_A', 
  '0277', 
  '0276', 
  '0173', 
  '0256', 
  'ITP1_3_B', 
  'ITP1_3_C', 
  '0003', 
  '0007', 
  '0521', 
  'ITP1_3_D', 

  '0000', 
  'ITP1_5_A', 
  'ITP1_5_B', 
  'ITP1_5_C', 
  'ITP1_4_C', 
  'ITP1_4_D', 
  '1147', 
  '0052', 
  'ALDS1_10_A', 
  'ALDS1_5_C', 

  'ITP1_6_A', 
  '0592', 
  '0619', 
  '0533', 
  '0511', 
  '0407', 
  '0516', 
  '0001', 
  '0028', 
  '0219', 

  '0020',
  'ITP1_8_A',
  'ITP1_8_C', 
  'ITP1_8_B', 
  '2271', 
  'ITP1_9_A', 
  'ITP1_8_D', 
  'ALDS1_14_A', 
  'ITP1_9_B', 
  'ITP1_9_C', 
  '0174', 

  'ITP1_10_A', 
  'ITP1_10_B', 
  'ITP1_10_C', 
  'ITP1_7_A', 
  'ITP1_7_B', 
  'ITP1_6_B', 
  'ITP1_6_D', 
  'ITP1_7_D', 
  'ITP1_7_C', 
  'ITP1_10_D', 

  'NTL_1_A', 
  'NTL_1_B', 
  '0197', 
  'NTL_1_C', 
  'ALDS1_1_B', 
  'ALDS1_1_C', 
  '0009', 
  '1200', 
  '0158', 
  '0014', 
  '0004', 
  '0080', 
  '2220', 

  '0084', 
  '0006', 
  '1042', 
  '1044', 
  '0522', 
  '0063', 
  '0512', 
  '0029', 
  '0050', 
  '0064', 
  '0025', 

  '1153', 
  '2197', 
  '1192', 
  '1616', 
  '1624', 
  '1172', 
  '2406', 
  '2331', 
  '1141', 

  '0208', 
  '2298', 
  '0317', 
  '1165', 
  '1186', 
  '1142', 
  '1601', 
  '1609', 
  '1193', 
  '2013', 
  '1173', 

  '2522', 
  '2772', 
  '0176', 
  '0287', 
  '0109', 
  '0506', 
  '0040', 
  '0077', 
  'ALDS1_10_C', 

  '0393', 
  '0033', 
  '1045', 
  '0008', 
  '0096', 
  '0030', 
  '0097', 
  '0092', 

  'ALDS1_1_D', 
  'ALDS1_3_A', 
  'ALDS1_3_B', 
  'ALDS1_4_A', 
  'ALDS1_4_B', 
  'ALDS1_4_D', 
  'ALDS1_3_D', 
  'ALDS1_5_A', 
  '0118', 
  'ALDS1_13_A', 
  'ALDS1_13_B', 
  '0168', 
  'DPL_1_A', 
  'DPL_1_B', 
  '2272', 

  '1130', 
  '1160', 
  '1610', 
  '1626', 
  '1167', 
  '1625', 
  '1161', 
  '1611', 
  '1131', 
  '1194', 
  '1144', 
  '1156', 
]

def getCode(l_userId, l_problemId):
  for problemId in l_problemId:
    for userId in l_userId:
      print('@@get: ', userId, problemId)
      collect_aoj.download(userId, problemId)

def trans_kotonoha(py_file):
  code = ''
  transpiler = kotonoha.Kotonoha()
  transpiler.load('python3:builtin:random')

  with open(py_file) as f:
    py_code = f.read()
    if py_code:
      code = transpiler.compile(py_code)
  return code

def trans_download(userId, problemId, py_file):
  code = trans_kotonoha(py_file)
  if code:
    with open(f'data/{userId}_kotonoha.py', 'a') as f:
      f.write('\n' + code)

def trans(l_userId, l_problemId):
  for problemId in l_problemId:
    for userId in l_userId:
      trans_download(userId, problemId, f'data/1231/{problemId}/{userId}_{problemId}.py')
      print('@@trans: ', userId, problemId)

if __name__ == '__main__':
  l_getProblemId = collect_aoj.get_problemId_list(l_userId[0]) # どこか別のところで事前にとらないとtrans 中のエラー時の回避が面倒
  getCode(l_userId, l_getProblemId)
  trans(l_userId, l_getProblemId)
