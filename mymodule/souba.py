comment = """
S&P500企業の実態がすごい！？アメリカ現地へ行ってきた  
https://youtu.be/dEDAEvjqBPo?si=8ccv9L_bOsvDNk2E  
S&P500はもう伸びない？AI関連企業の本社、新商品に注目、アメリカ現地で考察  
https://youtu.be/PpAppr_bL3M?si=08IrwrJkN7Nt1ctF  
"""
date="7/4"
#第一口座
mswap1 =21*22
usswap =24.2
ruikei1 =214182
saeki1 =294320
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/149128

#第二口座
mswap2 =2*23
leverage=3.75
tswap =81*37
ruikei2 =255608
saeki2 =98500
hyouka2 = ruikei2 + saeki2
yukou2 = (755349 + hyouka2)/170000

#投資信託
nikkei =40700
bull =19186
bear =717
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
81万通貨（取得平均単価4.851)  
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
