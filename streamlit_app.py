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

with st.container():
    st.header("Result")
    st.image("https://serverless-api-storage.runcomfy.net/deployment_requests/7f2ebf4d-ed40-4842-aba3-c91038b9cd36/output/ComfyUI_1765533995_00001_.png")


  








