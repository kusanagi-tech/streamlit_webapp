comment = """
🟠メキシコ・ペソ、下げ加速－大統領・議会選での左派与党圧勝後  
９円を切る大暴落です。  
🟠DMMビットコイン、流出事件の最新情報まとめ｜約482億円の行方とは - CRYPTO TIMES  
https://crypto-times.jp/explaining-dmm-bitcoin-outflow-as-of-6-2/  
"""
date="6/4"
#第一口座
usd =156.05
mxn =8.80
mswap1 =20*26
usswap =19.2
ruikei1 =196998
saeki1 =270199
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/147479

#第二口座
mswap2 =2*26
leverage=3.85
mytry =4.83
tswap =68*30
ruikei2 =163871
saeki2 =8680
hyouka2 = ruikei2 + saeki2
yukou2 = (655349 + hyouka2)/122000

#投資信託
nikkei =38700
bull =16223
bear =851
soneki = bull + bear - 15807

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
２万通貨（取得平均単価8.1)  
スワップ：{mswap2}円（推定)  
レバレッジ:{leverage}倍  
トルコリラ:{mytry}  
68万通貨（取得平均単価4.851)  
スワップ：{tswap:,}円(推定)  
累計スワップ：{ruikei2:,}円  
為替差益（含み益）：{saeki2:,}円  
評価損益：{hyouka2:,}円  
有効比率：{yukou2:.2%}  

日経平均先物相場：{nikkei:,}円  
◆楽天日本株4.3ブル（4,277口)   
評価額：{bull:,}円（資本金１.5万円)  
◆楽天日本株3.8倍ベアII(9,472口）  
評価額：{bear}円（資本金871円）  
リスクヘッジ後の概算損益:{soneki:,}円  
"""
