import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データ分析関連
df = pd.read_csv('./data/sample.csv')
st.dataframe(df)
st.line_chart(df)
st.bar_chart(df['2021'])

# matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df['2021'])
ax.set_title('matplotlib graph')
st.pyplot(fig)