comment = """
財務省、過去最大の為替介入　総額9.7兆円　4、5月に実施  
https://news.yahoo.co.jp/articles/0a6f5322b84594cd7b07b4a435018bb2a5f38892  
DMMからビットコイン482億円分が不正流出  
https://news.yahoo.co.jp/articles/c143a5d33a031af902d5e25b749095fa13b7749e  
為替介入の公式発表より、ビットコインの方が話題をさらいそうです。
"""
date="6/1"
#第一口座
usd =157.26
mxn =9.25
mswap1 =18*26
usswap =19.3
ruikei1 =196458
saeki1 =355024
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/122000

#第二口座
mswap2 =2*26
leverage=3.72
mytry =4.87
tswap =65*30
ruikei2 =161507
saeki2 =31410
hyouka2 = ruikei2 + saeki2
yukou2 = (655349 + hyouka2)/122000

#投資信託
nikkei =38730
bull =15448
bear =891
soneki = bull + bear - 15807

#フレーム部分
page01 = f"""
{date}のスワップ

メキシコ・ペソ相場：{mxn}  
18万通貨（取得平均単価7.3)  
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
65万通貨（取得平均単価4.851)  
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
