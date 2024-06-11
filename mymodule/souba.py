comment = """
トルコリラのスワップポイントは６日分の先払いです。メキシコペソは、8.4で引っかかって止まり、さすがに7円までは下がらないようです。暗号資産は、全体的に下がっています。
6月12日(水)午後9:30には重要経済指標「5月米消費者物価指数（CPI）」発表が予定されています。  
◆FXライブ  
https://www.youtube.com/live/CPctJG8RK6w?si=Jobk1iivz2RKMjKG
"""
date="6/12"
#第一口座
mswap1 =20*25*3
usswap =58.2
ruikei1 =201272
saeki1 =204328
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/142934

#第二口座
mswap2 =2*26*3
leverage=3.98
tswap =74*37*6
ruikei2 =184882
saeki2 =240
hyouka2 = ruikei2 + saeki2
yukou2 = (755349 + hyouka2)/156000

#投資信託
nikkei =38930
bull =16643
bear =829
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
74万通貨（取得平均単価4.852)  
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
