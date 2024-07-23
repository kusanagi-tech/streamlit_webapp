comment = """
7月末(30-31)になると、日銀金融政策決定会合とアメリカのFOMCが同日にあります。ここで相場が大きく動くでしょう。  
日銀：国債の買い入れ額の減少計画  
FOMC：政策金利の利下げ時期  
"""
date="7/23"
#第一口座
mswap1 =22*25
usswap =19.3
ruikei1 =223298
saeki1 =259305
hyouka1 = ruikei1 + saeki1
yukou1 = (839502/160368)

#第二口座
mswap2 =2*25
leverage=4.96
tswap =106*38
ruikei2 =316400
saeki2 =-96170
hyouka2 = ruikei2 + saeki2
yukou2 = (810878 + hyouka2)/220000	

#投資信託
nikkei =39860
bull =16721
bear =781
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
22万通貨（取得平均単価7.635)  
レバレッジ4.3倍  
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
106万通貨（取得平均単価4.844)  
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
