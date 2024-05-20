comment = """
ドル156円突破、トルコリラとメキシコペソ急上昇。
分散投資も大事ですが、分散投入も考えたほうがいいかもしれません。
"""
date="5/21"
#第一口座
usd =156.28
mxn =9.44
mswap1 =18*26
usswap =19.1
ruikei1 =190120
saeki1 =387159
#第二口座
mswap2 =2*26
leverage=3.35
mytry =4.83
tswap =52*35
ruikei2 =137246
saeki2 =22690
#投資信託
nikkei =39220
bull =16,599
bear =850
soneki =1642

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
52万通貨（取得平均単価4.847)  
スワップ：{tswap}円(推定)  
累計スワップ：{ruikei2:,}円  
為替差益：{saeki2:,}円  

日経平均先物相場：{nikkei:,}円  
楽天日本株4.3ブル（4,277口)   
評価額：{bull:,}円（資本金１.5万円)  
楽天日本株3.8倍ベアII(9,472口）  
評価額：{bear}円（資本金871円）  
リスクヘッジ後の概算損益:{soneki:,}円  
"""
