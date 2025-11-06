import streamlit as st
import numpy as np
import pandas as pd

st.write ("This is my first App in ISTM635")
st.title("Complexity Analysis Example")

df = pd.DataFrame(np.random.randn(500, 2)/[50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)  
df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])  
print(df)

st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

st.balloons()
st.progress(100)
st.spinner("This is a spinner")
st.sidebar.title("This is a sidebar title")
st.sidebar.header("This is a sidebar header")

st.image("/Users/terence/Downloads/chart_t1.png")
st.video("https://www.youtube.com/watch?v=V6mKVRU1evU")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.checkbox("This is a checkbox")
st.button("This is a button")
st.radio("This is a radio button", options=["Option 1", "Option 2", "Option 3"])
st.selectbox("This is a selectbox", options=["Choice A", "Choice B", "Choice C"])
st.multiselect("This is a multiselect", options=["Item 1", "Item 2", "Item 3"])
st.slider("This is a slider", min_value=0, max_value=100, value=50)
st.select_slider("This is a select slider", options=["Red", "Green", "Blue"], value="Green")    

st.header("Analyzing Time Complexity with Nested Loops")
st.markdown("This is a simple Streamlit app to demonstrate time complexity analysis using nested loops in Python.")
st.latex("E=mc^2")