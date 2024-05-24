comment = """
米ドルが157円を一時突破。169.9円周辺で上下を繰り返しています。
"""
date="5/27"
#第一口座
usd =156.962
mxn =9.39
mswap1 =18*26
usswap =19.2
ruikei1 =193024
saeki1 =377540
hyouka1 = ruikei1 + saeki1
yukou1 = (353009 + hyouka1)/122000

#第二口座
mswap2 =2*26
leverage=3.52
mytry =4.850
tswap =57*32
ruikei2 =148937
saeki2 =34580
hyouka2 = ruikei2 + saeki2
yukou2 = (655349 + hyouka2)/122000

#投資信託
nikkei =38800
bull =15708
bear =886
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
57万通貨（取得平均単価4.847)  
スワップ：{tswap:,}円(推定)  
累計スワップ：{ruikei2:,}円  
為替差益（含み益)：{saeki2:,}円  
評価損益：{hyouka2:,}円  
有効比率：{yukou2:.2%}  

日経平均先物相場：{nikkei:,}円  
楽天日本株4.3ブル（4,277口)   
評価額：{bull:,}円（資本金１.5万円)  
楽天日本株3.8倍ベアII(9,472口）  
評価額：{bear}円（資本金871円）  
リスクヘッジ後の概算損益:{soneki:,}円  
"""
