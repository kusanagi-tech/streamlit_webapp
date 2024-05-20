code1 ="""
#外為オンラインから為替相場を読み取るPython3プログラム
#Google Colaboratoryで実行できる。
 
import requests as req
from datetime import datetime, timedelta, timezone

URL = "http://www.gaitameonline.com/rateaj/getrate"
res  = req.get(URL)
ticker = res.json()

JST = timezone(timedelta(hours=+9), 'JST')
now = datetime.now(JST).strftime('%Y/%m/%d/ %H:%M:%S')

print(URL+'\\n')

#iは0から23までの整数 ドル円は20 ユーロ円は16

def get_ticker(i=20):
  base = ticker['quotes'][i]
  koumoku = ['bid','ask','open','high','low']
  print(base['currencyPairCode'] ,now)
  for i in koumoku:
    print(i.capitalize().rjust(5)+":",base[i])
  print("")

get_ticker()
get_ticker(3)
get_ticker(7)

#デバッグ用:コード一覧表取得
# res.status_code
# res.json()
# for i in range(len(ticker['quotes'])):
#   print(ticker['quotes'][i]['currencyPairCode'],i)
"""