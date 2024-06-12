comment = """
「5月米消費者物価指数（CPI）」発表直後にドルは156.3に急落し、米連邦公開市場委員会（ＦＯＭＣ）終了後、政策金利の据置の発表後急騰しました。”いってこいの動き”。メキシコペソは、現役の大統領が退任前に憲法改正を通すという発表で一段と下がりました。９円台で買わなくてよかったです。スワップと為替差益は両方利益なのですが、スワップは価格が変動しないので、スワップのほうが頼りになります。
"""
date="6/13"
#第一口座
mswap1 =20*26
usswap =19.4
ruikei1 =202890
saeki1 =179348
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/142934

#第二口座
mswap2 =2*26
leverage=4.04
tswap =75*37*0
ruikei2 =201688
saeki2 =-13930
hyouka2 = ruikei2 + saeki2
yukou2 = (755349 + hyouka2)/158000

#投資信託
nikkei =39200
bull =16224
bear =847
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
75万通貨（取得平均単価4.850)  
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
