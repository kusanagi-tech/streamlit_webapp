comment = """
メキシコペソは急上昇中で、戻りの相場に入っています。流石に急落しても7円台では買えませんでした。ドルが160円近くまで上昇しています。このためもらえるドルのスワップも5円ほど増えています。日銀の為替介入が再びくるのでしょうか？  
◆円相場1ドル＝159円台に　為替介入あった4月末以来 約2か月ぶりの円安水準  
https://youtu.be/2VY9COOXM1c?si=8QR15mVmqtXlC9lV  
◆コメの先物取引 大阪の取引所の申請 政府認可 8月新市場開設へ  
https://youtu.be/PJzcnPp0sR4?si=yoe46LQ2Y-Z5xyOc  
◆【｢S&P500｣｢NYダウ｣｢ナスダック｣って結局なにが違うの？】  
https://youtu.be/-yVbJVszc84?si=qF233djsz7UoAkor
"""
date="6/24"
#第一口座
mswap1 =21*25
usswap =24.2
ruikei1 =207855
saeki1 =282472
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/149128

#第二口座
mswap2 =2*26
leverage=4.13
tswap =79*37
ruikei2 =219324
saeki2 =14250
hyouka2 = ruikei2 + saeki2
yukou2 = (755349 + hyouka2)/166000

#投資信託
nikkei =38490
bull =15509
bear =873
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
79万通貨（取得平均単価4.850)  
スワップ：{tswap:,}円(推定)  
累計スワップ：{ruikei2:,}円  
為替差益：{saeki2:,}円  
評価損益：{hyouka2:,}円  
有効比率：{yukou2:.2%}  

日経平均先物相場：{nikkei:,}円  
◆楽天日本株4.3ブル（4,277口)   
評価額：{bull:,}円（資本金1.5万円)  
◆楽天日本株3.8倍ベアII(9,472口）  
評価額：{bear}円（資本金871円）  
リスクヘッジ後の概算損益:{soneki:,}円  
"""
