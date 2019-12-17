# SCORER Traffic Counter 車速計測スクリプト

## 概要

SCORER Traffic Counter の出力結果ログから車速を計測するスクリプトです。下記のイメージのように、２本の検知線を引き、検知線の間の距離を入力頂くと車速が出力されます。
![image](https://user-images.githubusercontent.com/4166534/70995489-ffec6880-2113-11ea-8778-14c23d40bef0.png)

なお、検知線間の距離に関しては、白線などを目印にして頂くか、実際に計測を頂く必要があります。
![download](https://user-images.githubusercontent.com/4166534/70995877-e8fa4600-2114-11ea-979d-9f476a9dded3.png)

## 

```
# arguments: measure.py [csvfile] [distance(meter)]
python3 measure.py sample.csv 100 > output.csv
```
