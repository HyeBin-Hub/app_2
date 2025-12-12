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
col_left, divider, col_right = st.columns([1, 0.5, 2])

with col_left:
  
  st.header("Shot Settings")

  with st.expander("Image Size Setting"):
      width = st.selectbox("Width", [256, 512, 768, 1024], index = 1)
      height = st.selectbox("Height", [256, 512, 768, 1024], index = 1)
    
  with st.expander("Seed Setting"):
      steps = st.slider("Steps", 10, 40, 20)
      cfg = st.slider("CFG", 1.0, 15.0, 8.0, step=0.5)
    
      st.subheader("Advanced")
      seed_mode = st.radio("Seed mode", ["Random", "Fixed"], index=0)
      if seed_mode == "Fixed":
        fixed_seed = st.number_input("Fixed seed", min_value=0, value=42, step=1)
      else:
        fixed_seed = None

  ########################################################################################
  # Main Inputs 
  ########################################################################################
  prompt = st.text_area(
    "Prompt", 
    value = "cinematic film still, cyberpunk city, rain, neon lights, 8k, masterpiece", 
    height=120,
  )
  
  negative = st.text_area(
      "Negative Prompt",
      value="text, watermark, blurry, lowres",
      height=80,
  )
            
with col_right:
    st.header("Result")
    st.image("https://serverless-api-storage.runcomfy.net/deployment_requests/7f2ebf4d-ed40-4842-aba3-c91038b9cd36/output/ComfyUI_1765533995_00001_.png")


col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("Style preset", ["None", "Cinematic", "Anime", "3D Render"], index=1)
with col2:
    shot_size = st.selectbox("Shot size", ["Wide", "Medium", "Close-up"], index=0)

# ----------------------------
# Session State (버튼 중복 클릭 방지)
# ----------------------------
if "busy" not in st.session_state:
    st.session_state.busy = False

# ----------------------------
# Generate 버튼
# ----------------------------
generate = st.button("Generate", type="primary", use_container_width=True, disabled=st.session_state.busy)













