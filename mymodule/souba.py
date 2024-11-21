comment = """

"""
date="11/22"
#第一口座
mswap1 =5*21
usswap =0
tswap1 = 4*40
ruikei1 =7436
saeki1 =-2430
hyouka1 = ruikei1 + saeki1
yukou1 = (140000 + hyouka1)/44865

#第二口座
mswap2 =2*24
leverage=6.13
tswap2 =22*40
ruikei2 =19344
saeki2 =5500
hyouka2 = ruikei2 + saeki2
yukou2 = (810878 + hyouka2)/228000

#投資信託
nikkei =38230
bull =22144
bear =0
soneki = bull -26869

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

🇲🇽メキシコ・ペソ相場：{mxn}  
5万通貨（取得平均単価7.57)  
スワップ：{mswap1}円  
🇹🇷トルコリラ:{mytry}  
4万通貨（取得平均単価4.48)  
レバレッジ約6倍  
スワップ：{tswap1:,}円  
累計スワップ：{ruikei1:,}円  
為替差益（含み益）：{saeki1:,}円  
評価損益：{hyouka1:,}円  
有効比率：{yukou1:.2%}  　

第二口座  
🇹🇷トルコリラ  
22万通貨（取得平均単価4.41)  
レバレッジ:{leverage}倍  
スワップ：{tswap2:,}円(推定)  
累計スワップ：{ruikei2:,}円  
スポット評価：{saeki2:,}円  
評価損益：{hyouka2:,}円  
有効比率：{yukou2:.2%}  

💴日経平均先物相場：{nikkei:,}円  
◆楽天日本株4.3ブル（10,198口)   
評価額：{bull:,}円  
損益：{soneki:,}円

"""

#米ドル（臨時雇い）:{usd}円  
#千通貨（取得平均単価138.930)    
#スワップ:{usswap}円

#メキシコ・ペソ  
#2万通貨（取得平均単価8.1)  
#スワップ：{mswap2}円（推定)  
#レバレッジ:{leverage}倍  

#◆楽天日本株3.8倍ベアII(9,472口）  
#評価額：{bear}円（資本金871円）  
#リスクヘッジ後の概算損益:{soneki:,}円  
