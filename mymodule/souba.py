comment = """
為替相場は全体的に下がっています。 
"""
date="6/5"
#第一口座
usd =154.82
mxn =8.65
mswap1 =20*78
usswap =57.0
ruikei1 =197537
saeki1 =239985
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/147479

#第二口座
mswap2 =2*26*3
leverage=4.31
mytry =4.73
tswap =69*34*3
ruikei2 =166407
saeki2 =-75450
hyouka2 = ruikei2 + saeki2
yukou2 = (655349 + hyouka2)/122000

#投資信託
nikkei =38440
bull =15882
bear =867
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
69万通貨（取得平均単価4.852)  
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
