comment = """
為替相場全体が下がりましたが、まだ利益が残っていてよかったです。
"""
date="7/25"
#第一口座
mswap1 =22*25
usswap =18.9
ruikei1 =225507
saeki1 =173285
hyouka1 = ruikei1 + saeki1
yukou1 = (839502/160368)

#第二口座
mswap2 =2*25*3
leverage=5.47
tswap =108*38
ruikei2 =332940
saeki2 =-197900
hyouka2 = ruikei2 + saeki2
yukou2 = (810878 + hyouka2)/224000

#投資信託
nikkei =38170
bull =16060
bear =807
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
108万通貨（取得平均単価4.842)  
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
