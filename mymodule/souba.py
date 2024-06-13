comment = """
本日は日銀金融政策決定会合の二日目で、政策金利が発表されます。据置（0-0.1％）との予想があるのですが、内容によっては大幅な相場の変動があるかもしれません。（時間は未定で、昼頃との見込み。）ドルとメキシコペソのスワップは2日分の支給です。メキシコペソは戻しが入ってきて相場が上昇トレンドに入っています。
"""
date="6/14"
#第一口座
mswap1 =20*26*2
usswap =38.6
ruikei1 =203429
saeki1 =211112
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/142934

#第二口座
mswap2 =2*26*2
leverage=4.09
tswap =76*37*0
ruikei2 =201740
saeki2 =-16900
hyouka2 = ruikei2 + saeki2
yukou2 = (755349 + hyouka2)/160000

#投資信託
nikkei =38570
bull =15796
bear =867
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
20万通貨（取得平均単価7.536)  
レバレッジ3倍  
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
76万通貨（取得平均単価4.850)  
スワップ：{tswap:,}円(推定)  
累計スワップ：{ruikei2:,}円  
為替差損：{saeki2:,}円  
評価損益：{hyouka2:,}円  
有効比率：{yukou2:.2%}  

日経平均先物相場：{nikkei:,}円  
◆楽天日本株4.3ブル（4,277口)   
評価額：{bull:,}円（資本金1.5万円)  
◆楽天日本株3.8倍ベアII(9,472口）  
評価額：{bear}円（資本金871円）  
リスクヘッジ後の概算損益:{soneki:,}円  
"""
