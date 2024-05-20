date="5/20"
#第一口座
usd =155.75
mxn =9.38

mswap1 =468
usswap =19
ruikei1 =189633
saeki1 =376022
#第二口座
mswap2 =52
leverage=3.35
mytry =4.822
tswap =1820
ruikei2 =135374
saeki2 =13290

nikkei =38760
bull =16013
bear =879
soneki =1085

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
comment = """
円安なことは円安ですが、注意しないといけないのは、香港ドルやNZドルに対しても円は安くなっています。ざっくり試算してみるとこの5年間の円安で、68％に円が目減りしています。ドル建てで海外のお支払をする場合、5年前は1000万円だったのに、132％のお支払い、実際は現在1320万円払わないといけないんですよ。
"""