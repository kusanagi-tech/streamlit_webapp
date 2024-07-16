comment = """
暗号資産が急上昇しています。トランプ氏銃撃事件の影響だと言われています。
為替介入でトルコリラの相場が巻き戻ったので、トータルで100万通貨になるように買い足しました。しかし脅威は為替介入だけではなく、他の金融恐慌もあるので、注意が必要です。
"""
date="7/17"
#第一口座
mswap1 =21*25*3
usswap =58.2
ruikei1 =219982
saeki1 =309803
hyouka1 = ruikei1 + saeki1
yukou1 = (882317/156917)

#第二口座
mswap2 =2*25*3
leverage=4.70
tswap =100*38*3
ruikei2 =292730
saeki2 =-49250
hyouka2 = ruikei2 + saeki2
yukou2 = (810878 + hyouka2)/208000

#投資信託
nikkei =41500
bull =20281
bear =666
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
100万通貨（取得平均単価4.850)  
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
