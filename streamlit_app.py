import time
import streamlit as st


st.set_page_config(
  page_title = "Storyborad Generator",
  layout = "wide"
)

########################################################################################
# Header 설정 
########################################################################################
st.title("Storyboard Generator")
st.caption("시나리오를 Shot 단위로 분해하고, AI로 영화 스토리보드를 생성하세요.")

########################################################################################
# Sidebar 설정
########################################################################################
# with st.sidebar:
#   st.header("Settings")
#   width = st.selectbox("Width", [256, 512, 768, 1024], index = 1)
#   height = st.selectbox("Height", [256, 512, 768, 1024], index = 1)
#   steps = st.slider("Steps", 10,40,20)
#   cfg = st.slider("CFG", 1.0,15.0,8.0, step = 0.5)

col1, col2 = st.columns(2)

with col1:
    st.write("왼쪽")

with col2:
    st.write("오른쪽")


  








