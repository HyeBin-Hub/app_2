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

# with st.container():
#     st.header("Result")
#     st.image("https://serverless-api-storage.runcomfy.net/deployment_requests/7f2ebf4d-ed40-4842-aba3-c91038b9cd36/output/ComfyUI_1765533995_00001_.png")


# tab1, tab2 = st.tabs(["Storyboard", "Logs"])

# with tab1:
#     st.write("이미지")

# with tab2:
#     st.text("로그 출력")



# with st.form("my_form"):
#     prompt = st.text_area("Prompt")
#     submitted = st.form_submit_button("Generate")


col_left, col_right = st.columns([1, 2])
with st.container():
  with col_left:
    st.header("Shot Settings")
    width = st.selectbox("Width", [256, 512, 768, 1024], index = 1)
    height = st.selectbox("Height", [256, 512, 768, 1024], index = 1)
    steps = st.slider("Steps", 10, 40, 20)
    cfg = st.slider("CFG", 1.0, 15.0, 8.0, step=0.5)
  
    st.subheader("Advanced")
    seed_mode = st.radio("Seed mode", ["Random", "Fixed"], index=0)
    fixed_seed = st.number_input("Fixed seed", min_value=0, value=42, step=1)
    

with col_right:
    st.header("Result")
    st.image("https://serverless-api-storage.runcomfy.net/deployment_requests/7f2ebf4d-ed40-4842-aba3-c91038b9cd36/output/ComfyUI_1765533995_00001_.png")





