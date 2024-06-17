import streamlit as st
import pandas as pd
import scray
import plot

csvfile = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
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
    df = pd.read_csv(csvfile, encoding='shift-jis')
    st.dataframe(df, column_config={
        "URL": st.column_config.LinkColumn(
                "URL", 
                display_text="Open Site"
            )})
    st.pyplot(plot.plot())
else:
    st.write('ファイルをアップロードしてください')
