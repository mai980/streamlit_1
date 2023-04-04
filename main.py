import streamlit as st
import pandas as pd
import time
from PIL import Image

st.title('Streamlit 入門')

st.write('プログレスバーの表示')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
st.write('Done!!!')

expander1 = st.expander('1')
expander1.write('1テスト')
expander2 = st.expander('2')
expander2.write('2テスト')
expander3 = st.expander('3')
expander3.write('3テスト')
