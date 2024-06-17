import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

def getcsv():
    csvfile = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
    df = pd.read_csv(csvfile, encoding='shift-jis')
    return df
try:
    csvfile = getcsv()
    
    df = csvfile
    
    fig, ax = plt.subplots()
    
    c1,c2,c3,c4,c5 = "blue","green","red","black", "purple"
    l1,l2,l3,l4,l5 = 'モノタロウ', 'ヨドバシ', 'チャーム', 'ココデカウ', 'ビックカメラ'
    
    x1 = df[df['place'] == l1]['Date']
    x2 = df[df['place'] == l2]['Date']
    x3 = df[df['place'] == l3]['Date']
    x4 = df[df['place'] == l4]['Date']
    x5 = df[df['place'] == l5]['Date']
    
    y1 = df[df['place'] == l1]['price(tax included)']
    y2 = df[df['place'] == l2]['price(tax included)']
    y3 = df[df['place'] == l3]['price(tax included)']
    y4 = df[df['place'] == l4]['price(tax included)']
    y5 = df[df['place'] == l5]['price(tax included)']
    
    ax.set_title('価格推移')
    ax.grid() 
    
    ax.plot(x1, y1, color=c1, label=l1, marker='o',)
    ax.plot(x2, y2, color=c2, label=l2, marker='o',)
    ax.plot(x3, y3, color=c3, label=l3, marker='o',)
    ax.plot(x4, y4, color=c4, label=l4, marker='o',)
    ax.plot(x5, y5, color=c5, label=l5, marker='o',)
    ax.legend(loc=0)    # 凡例
    fig.tight_layout()  # レイアウトの設定
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    
    st.title('チモシー価格表')
    md = """
    ### 取得元
    - モノタロウ
    - ヨドバシ
    - チャーム
    - ココデカウ
    - ビックカメラ
    """
    st.markdown(md)
    
    if csvfile is not None:
        st.dataframe(csvfile, column_config={
            "URL": st.column_config.LinkColumn(
                    "URL", 
                    display_text="Open Site"
                )})
        st.pyplot(plt)
    else:
        st.write('ファイルをアップロードしてください')
except:
    st.write('wait')
