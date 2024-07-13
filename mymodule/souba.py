comment = """
NY外為 円相場が一時1円50銭ほど急騰　政府・日銀 2日連続で為替介入か｜TBS NEWS DIG  
https://youtu.be/gPOTccE3Aus?si=mshSwq2EqHpYwRdi  
為替介入の推定は、日銀の当座預金の残高から推定して報道している記事もあります。  
７月15日は祝日なので、東京市場の資金の流動性が少なく相場を操作しやすくなります。三度目の正直はあるのでしょうか？  
"""
date="7/15"
#第一口座
mswap1 =21*25
usswap =20.2
ruikei1 =218893
saeki1 =308675
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/149128

#第二口座
mswap2 =2*25
leverage=4.45
tswap =95*38
ruikei2 =285296
saeki2 =-62100
hyouka2 = ruikei2 + saeki2
yukou2 = (755349 + hyouka2)/198000

#投資信託
nikkei =41190
bull =20138
bear =670
soneki = bull + bear - 15807

#為替レートの自動取得
import requests as req
def currency_ask(x,y = 'ask'):
  URL = """https://forex-api.coin.z.com/public/v1/ticker"""
  res = req.get(URL)
  ticker = res.json()['data']
  return ticker[x][y]

usd = currency_ask(0)
mytry = currency_ask(8)
mxn = currency_ask(10)

#フレーム部分
page01 = f"""
{date}のスワップ

メキシコ・ペソ相場：{mxn}  
21万通貨（取得平均単価7.582)  
レバレッジ2.31倍  
スワップ：{mswap1}円  
米ドル（臨時雇い）:{usd}円  
千通貨（取得平均単価138.930)    
スワップ:{usswap}円  
累計スワップ：{ruikei1:,}円  
為替差益（含み益）：{saeki1:,}円  
評価損益：{hyouka1:,}円  
有効比率：{yukou1:.2%}  　

第二口座  
メキシコ・ペソ  
2万通貨（取得平均単価8.1)  
スワップ：{mswap2}円（推定)  
レバレッジ:{leverage}倍  
トルコリラ:{mytry}  
95万通貨（取得平均単価4.855)  
スワップ：{tswap:,}円(推定)  
累計スワップ：{ruikei2:,}円  
スポット評価：{saeki2:,}円  
評価損益：{hyouka2:,}円  
有効比率：{yukou2:.2%}  

日経平均先物相場：{nikkei:,}円  
◆楽天日本株4.3ブル（4,277口)   
評価額：{bull:,}円（資本金1.5万円)  
◆楽天日本株3.8倍ベアII(9,472口）  
評価額：{bear}円（資本金871円）  
リスクヘッジ後の概算損益:{soneki:,}円  
"""
