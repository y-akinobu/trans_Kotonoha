# userId とprobelmId からデータを抜くスクリプト
from collections import Counter
import os
import requests
import json
import sys
import csv,time
from datetime import datetime

status = [
    'CE', #COMPILEERROR', = 0
    'WA', #WRONGANSWER= 1
    'TLE', #TIMELIMIT= 2
    'MLE', #MEMORYLIMIT= 3
    'AC', #ACCEPTED= 4
    'WAIT', #WAITING= 5
    'OLE', # OUTPUTLIMIT= 6
    'RE', #RUNTIMEERROR= 7
    'PE', #PRESENTATIONERROR= 8
    'RUN',
]

l_problemId = []

def day(ts):
    return datetime.fromtimestamp(ts//1000).strftime('20%y/%m/%d')

def add_record(entry):
  row = []
  row.append(entry['judgeId'])
  row.append(entry['userId'])
  row.append(entry['problemId'])
  row.append(day(entry['submissionDate']))
  row.append(entry['language'])
  row.append(status[entry['status']])
  return row

def get_problemId_list(user):
  url = "https://judgeapi.u-aizu.ac.jp/submission_records/users/" + user + "?size=2000"
  r = requests.get(url)
  if r.status_code != 200:
    return ''
  data = json.loads(r.text)
  for entry in data:
    if entry['status'] == 4 and entry['language'] == 'Python3':
      l_problemId.append(entry['problemId'])
      time.sleep(1)
  return l_problemId

def get_judge(judgeId):
  url = f'https://judgeapi.u-aizu.ac.jp/reviews/{judgeId}'
  r = requests.get(url)
  if r.status_code != 200:
    print(judgeId, r.status_code)
    return ''
  data = json.loads(r.text)
  return data.get('sourceCode', '')

def get_code(userId, problemId):
  record = []
  code = ''
  url = "https://judgeapi.u-aizu.ac.jp/submission_records/users/" + userId + "/problems/" + problemId + "?size=10"
  r = requests.get(url)
  if r.status_code != 200:
    print(userId, r.status_code)
    return ''
  data = json.loads(r.text)
  for entry in data:
    if entry['language'] == 'Python3' and entry['status'] == 4:
      record = add_record(entry)
    if record:
      time.sleep(1)
      code = get_judge(record[0])
      if code.startswith('You are not'):
        code = ''
      break
  return code

def download(userId, problemId):
  os.makedirs(f'data/groupB/{problemId}', exist_ok=True)
  with open(f'data/groupB/{problemId}/{userId}_{problemId}.py', 'w') as f:
    f.write(get_code(userId, problemId))

# def download2(userId, problemId):
#   with open(f'data/{userId}.py', 'a') as f:
#     f.write('\n' + get_code(userId, problemId))

if __name__ == '__main__':
  for userId in sys.argv[1:]:
    download(userId, '0004')
