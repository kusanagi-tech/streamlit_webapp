comment = """
暗号資産の相場は昨年度にくらべて上昇しています。
"""
date="6/6"
#第一口座
usd =155.680
mxn =8.896
mswap1 =20*26
usswap =19.3
ruikei1 =199155
saeki1 =288424
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/147479

#第二口座
mswap2 =2*26
leverage=4.09
mytry =4.796
tswap =70*36
ruikei2 =174123
saeki2 =-9960
hyouka2 = ruikei2 + saeki2
yukou2 = (655349 + hyouka2)/122000

#投資信託
nikkei =38440
bull =15475
bear =886
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
2万通貨（取得平均単価8.1)  
スワップ：{mswap2}円（推定)  
レバレッジ:{leverage}倍  
トルコリラ:{mytry}  
70万通貨（取得平均単価4.852)  
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
