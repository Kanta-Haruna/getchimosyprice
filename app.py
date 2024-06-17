import streamlit as st
import pandas as pd
import scray
import plot

csvfile = '/Users/harunakanta/PythonTraining/csv/chimosy.csv'
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

df = pd.read_csv(csvfile, encoding='shift-jis')

st.dataframe(df, column_config={
    "URL": st.column_config.LinkColumn(
            "URL", 
            display_text="Open Site"
        )})


st.pyplot(plot.plot())



if st.button('click'):
    scray.makedf()
else:
    st.write('スクレイピングを実行したい場合、クリックしてください。')
