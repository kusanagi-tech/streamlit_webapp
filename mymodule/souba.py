comment = """
高い・・・。やはり安い時に赤字の時にせっせと買い貯め。
ビットコインが相場40万円の時に一千万円まで上がると予想した人がいるんですよ。まさかと思ったんですけど。何かの根拠があったのかもしれません。  
◆日経平均は「◯万円」まで上がる？  
https://youtu.be/Ij1uJF-XqeE?si=Z9l7V5rxU4lfQwu7  
ーブラックスワン（予測不可の金融恐慌の原因）  
◆ドル円、38年ぶり高値を更新、162円が視野に  
https://youtu.be/99PVz18abq4?si=vuVHXjQrCOIHx8M2 　　
"""
date="7/3"
#第一口座
mswap1 =21*25*0
usswap =73.2
ruikei1 =214109
saeki1 =285362
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/149128

#第二口座
mswap2 =2*26*0
leverage=3.83
tswap =80*37*3
ruikei2 =246488
saeki2 =100800
hyouka2 = ruikei2 + saeki2
yukou2 = (755349 + hyouka2)/168000

#投資信託
nikkei =40210	
bull =18229
bear =752
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
