import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit Hello Yoshiki')

st.write("Most objects")

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
}) # データフレームの作成

st.write(df)  # データフレームの表示
st.dataframe(df.style.highlight_max(axis=0), width=300, height=300) # データフレームの表示（スタイル付き）

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.write('DataFrame') # テキストの表示

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)   
# データフレームの作成
# (20, 3)の引数は、20行3列の2次元配列を作成するよう指定
# rand関数は、0から1の間の一様分布に従うランダムな浮動小数点数を生成。
st.write(df2)  # データフレームの表示

# df2に対して、数字の範囲を指定し、行ラベルを指定するd3を作成する

# 行ラベルを指定するリスト
row_labels = ['d', 'e', 'f', 'g', 'h']

# 生成するランダム値の範囲を[a, b]とする
a = 100
b = 1000

df3 = pd.DataFrame(
    np.random.rand(5, 3) * (b - a) + a,
    columns=['a', 'b', 'c'],
    index=row_labels
)
st.write(df3)

st.line_chart(df2) # 折れ線グラフの表示
st.area_chart(df3) # エリアグラフの表示

df4 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df4) # 地図の表示

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.write('Display Image') #画像の表示

img = Image.open('/Users/miyazawayoshiki/Downloads/20240319_ver1.2.2/03_webアプリ作成/pic/img031.jpg') 
# 画像の読み込み(絶対パスで記載)

st.image(img, caption='sample', use_column_width=True) # 画像の表示

text = st.sidebar.text_input('あなたの趣味を教えてください。') # テキスト入力
'私の趣味は', text, 'です。' # テキスト表示

# レイアウトとして２列を定義
col1, col2 = st.columns(2)
# 1列目をwithで囲む
with col1:
    st.write("列1がここに表示されます")

# 2列目をwithで囲む
with col2:
    st.write("列2がここに表示されます")

st.sidebar.write("hello world") #.sidebar付けるとサイトバーに出力されます。
st.text_input("ここに文字が入力できます。") # テキストを入力できます。

slider_text = st.slider("スライダーで数字を決定できます。",0,100,5) # (最小、最大値、デフォルト値)の順で設定されます。
"スライダーの数字:",slider_text

st.button("ボタン") # ボタンが設置されます。

import time # 時間を扱う機能をインポート

x = st.empty() # 文字が出力される場所をあらかじめ確保します。その場所をxとしています。
bar = st.progress(0) # 進捗0のプログレスバーを出力します。

# iに0から99まで代入しながら実行されます
for i in range(100):
    time.sleep(0) # 0秒待機します。
    x.text(i) # 確保した場所xに代入されたiの値を代入します。
    bar.progress(i) # 進捗iに変更します。
    i += 1 # iに1足し算して代入します。

# 選択肢を配列で指定して選択肢を出力します。
st.selectbox("選んでください。",["選択肢1","選択肢2","選択肢3"])

# ダウンロードする文字を定義し、output_textに代入します。
output_text = "この文字がダウンロードされますよ！！！"

 # 代入された文字をダウンロードするボタンを設置。オプションは内容をdataに指定、ファイル名をfile_nameに指定、ファイルタイプをmimeに指定
st.download_button(label='記事内容 Download', 
                   data=output_text, 
                   file_name='out_put.txt',
                   mime='text/plain',
                   )

# ファイルアップローダーを設置します。typeでアップロードできるファイルの種類を指定できます。
file_upload = st.file_uploader("ここに音声認識したファイルをアップロードしてください。",type=["png","jpg"])

# ファイルがアップロードされた時にその画像を表示します。
if (file_upload !=None):
    st.image(file_upload)# 画像を表示します。

# 乱数の配列を作るメソッドを作ります。引数r,cとし、それぞれおのデフォルト値を10と5に設定します。
def rand_df6(r=10, c=5):
    df6 = pd.DataFrame(
        np.random.randn(r, c),
        columns=('col %d' % i for i in range(c)))# 乱数10の５個の数列を作ります。カラムの設定は0-4の名前を付けます。
    return df6 # 作ったデータフレームを返します。
dataframe = rand_df6(r=10,c=3) # rに10、cに3を代入したrand_dfメソッドを処理します。

# 表の描画します。
st.dataframe(dataframe.head(n=3))
# データフレームのチャートの描画します。
st.line_chart(dataframe)