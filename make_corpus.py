import os
import sys
import collect_aoj

l_userId = [
  'jakenu0x5e', 'tefu417', 'baron2', 'kuwaaaaaaaaaaaaaaaaa', 'kichi941', 
  'bal4u', 'cima', 'novel', 'tricom', 'tige', 
  'KubotaNoriko1230', 'pypy', 'HiroN', 'bs5lNkJ',
  'manaka', 'puyopop', 'RandyWaterhouse', 'yoheikikuta', 'tsuru_aji', 'bonoron', 'doorgod', 
  'Mackie', 'y1721', 'tkawata', 'peroon', 'leeav_ten', 'momiji6', 'meiadayz', 'yreb', 
  'misuta', 'n_knuu', 'mxg7y', 'rockbirds12', 'zywuwen', 'halfpennyworths',
  'SMON', 'shana', 'nananashi', 'vjudge2', 'takumiy', 'rune', 'PythonHolic', 
  'kira924age', 'sota1235', 'soutatahara', 'tappinasa', 'tallestorange', 'Sim0000', 
  'toyuzuko', 'jj1guj', 'nut5ch3st', 'Fulltea'
]

def get_l_problemId(userId):
  with open(f'data/probId_list/{userId}_list.txt') as f:
    text = f.read()

  text = text.replace('\'', '')
  text = text.replace('\n', '')
  text = text.replace('[', '')
  text = text.replace(']', '')
  l_problemId = text.split(', ')

  return l_problemId

# def getCode(userId, l_problemId):
#   for problemId in l_problemId:
#     print('@@get: ', userId, problemId)
#     code = collect_aoj.get_code(userId, problemId)
#   return code

if __name__ == '__main__':
  for userId in l_userId:
    l_problemId = get_l_problemId(userId)
    for problemId in l_problemId:
      print('@@get: ', userId, problemId)
      code = collect_aoj.get_code(userId, problemId)

      with open(f'data/raw/{userId}.py', 'a') as f:
        f.write('\n' + code)
