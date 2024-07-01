comment = """
いきなり高くなった・・・・。今週は変則的なスワップの配布になっています。  
今までトルコリラのレバレッジは15倍以下に制限されていた所が多かったのですが、法定上限(個人)の25倍の取引許可を出すところが増えて来ました。  
https://lightfx.jp/press/20240701-1/  
【買いオペってなに？】日銀の国債買い入れ減額ってなんなの？  
https://youtu.be/WM-xwgq9Gs8?si=clcSW-vaoJgVQsIZ  　　
"""
date="7/2"
#第一口座
mswap1 =21*25*3
usswap =0
ruikei1 =212723
saeki1 =272544
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/149128

#第二口座
mswap2 =2*26*3
leverage=3.83
tswap =80*37*0
ruikei2 =246350
saeki2 =81320
hyouka2 = ruikei2 + saeki2
yukou2 = (755349 + hyouka2)/168000

#投資信託
nikkei =39480 	
bull =17399
bear =784
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
80万通貨（取得平均単価4.850)  
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
