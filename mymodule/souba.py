comment = """
スワップの支給は4日分の予定となっています。
"""
date="5/22"
#第一口座
usd =156.15
mxn =9.38
mswap1 =18*104
usswap =76
ruikei1 =190607
saeki1 =377135
#第二口座
mswap2 =2*104
leverage=3.37
mytry =4.840
tswap =53*35*4
ruikei2 =139153
saeki2 =25730
#投資信託
nikkei =38870
bull =16361
bear =861
soneki =1415

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

第二口座  
メキシコ・ペソ  
２万通貨（取得平均単価8.1)  
スワップ：{mswap2}円（推定)  
レバレッジ:{leverage}倍  
トルコリラ:{mytry}  
53万通貨（取得平均単価4.847)  
スワップ：{tswap:,}円(推定)  
累計スワップ：{ruikei2:,}円  
為替差益：{saeki2:,}円  

日経平均先物相場：{nikkei:,}円  
楽天日本株4.3ブル（4,277口)   
評価額：{bull:,}円（資本金１.5万円)  
楽天日本株3.8倍ベアII(9,472口）  
評価額：{bear}円（資本金871円）  
リスクヘッジ後の概算損益:{soneki:,}円  
"""
