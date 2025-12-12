import time
import streamlit as st
from workflow import runcomfy_generate_image

api_key = st.secrets.get("RUNCOMFY_API_KEY", "")
deployment_id = st.secrets.get("RUNCOMFY_DEPLOYMENT_ID", "")

if not api_key or not deployment_id:
    st.error("Secrets에 RUNCOMFY_API_KEY / RUNCOMFY_DEPLOYMENT_ID를 설정해야 합니다.")
    st.stop()
  
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
col_left, divider, col_right = st.columns([1, 0.3, 2])

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

    # ----------------------------
    # Session State (버튼 중복 클릭 방지)
    # ----------------------------
    if "busy" not in st.session_state:
        st.session_state.busy = False
    
    if generate:
        st.session_state.busy = True
        try:
            status_box = st.empty()
            status_box.info("Submitting...")
            with st.spinner("Generating..."):
                request_id, seed, image_url = runcomfy_generate_image(
                    api_key=api_key,
                    deployment_id=deployment_id,
                    prompt=prompt,
                    negative=negative,
                    poll_interval=poll_interval,
                    width=width,
                    height=height,
                    steps=steps,
                    cfg=cfg,
                    denoise=denoise,
                    sampler_name=sampler_name,
                    scheduler=scheduler,
                )
            status_box.success(f"Done | request_id={request_id} | seed={seed}")
            st.image(image_url, caption=image_url, use_container_width=True)
    
        except Exception as e:
            st.error(f"Failed: {e}")
        finally:
            st.session_state.busy = False
    
        
  # ----------------------------
  # Generate 버튼
  # ----------------------------
  generate = st.button("Generate", 
                       type="primary", 
                       use_container_width=True, 
                       disabled=st.session_state.busy)
  
            
with col_right:
    st.header("Result")
    st.image("https://serverless-api-storage.runcomfy.net/deployment_requests/7f2ebf4d-ed40-4842-aba3-c91038b9cd36/output/ComfyUI_1765533995_00001_.png")









