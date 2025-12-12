import time
import random
import requests
import streamlit as st

BASE_URL = "https://api.runcomfy.net/prod/v1"

def runcomfy_generate_image(
    api_key: str,
    deployment_id: str,
    prompt: str,
    negative: str,
    poll_interval: int,
    width: int,
    height: int,
    steps: int,
    cfg: float,
    denoise: float,
    sampler_name: str,
    scheduler: str,
):
    headers = {
        "Authorization": f"Bearer {api_key.strip()}",
        "Content-Type": "application/json",
    }

    nonce = int(time.time())
    seed = random.randint(1, 2**31 - 1)

    # ✅ 당신 workflow_api.json 기준 노드 ID
    payload = {
        "overrides": {
            "6": {"inputs": {"text": prompt}},  # positive
            "7": {"inputs": {"text": negative}},  # negative
            "3": {"inputs": {  # KSampler
                "seed": seed,
                "steps": steps,
                "cfg": cfg,
                "denoise": denoise,
                "sampler_name": sampler_name,
                "scheduler": scheduler,
            }},
            "5": {"inputs": {"width": width, "height": height, "batch_size": 1}},
            "9": {"inputs": {"filename_prefix": f"ComfyUI_{nonce}"}},
        }
    }

    # 1) submit
    submit_res = requests.post(
        f"{BASE_URL}/deployments/{deployment_id}/inference",
        headers=headers,
        json=payload,
        timeout=60,
    )
    submit_res.raise_for_status()
    request_id = submit_res.json()["request_id"]

    # 2) poll
    while True:
        st_res = requests.get(
            f"{BASE_URL}/deployments/{deployment_id}/requests/{request_id}/status",
            headers=headers,
            timeout=60,
        )
        st_res.raise_for_status()
        status_data = st_res.json()
        status = (status_data.get("status") or "").lower()

        if status in ("succeeded", "completed"):
            break
        if status in ("failed", "error"):
            raise RuntimeError(f"Run failed: {status_data}")

        time.sleep(poll_interval)

    # 3) result
    result_res = requests.get(
        f"{BASE_URL}/deployments/{deployment_id}/requests/{request_id}/result",
        headers=headers,
        timeout=60,
    )
    result_res.raise_for_status()
    result_data = result_res.json()

    # 4) parse output url (outputs is dict)
    image_url = None
    outputs = result_data.get("outputs", {})

    # Prefer SaveImage node "9"
    if isinstance(outputs, dict) and "9" in outputs:
        imgs = outputs["9"].get("images", [])
        if imgs:
            image_url = imgs[0].get("url")

    # Fallback: first node that has images
    if not image_url and isinstance(outputs, dict):
        for node_out in outputs.values():
            imgs = node_out.get("images", [])
            if imgs:
                image_url = imgs[0].get("url")
                break

    if not image_url:
        raise ValueError(f"이미지 URL을 찾지 못했습니다. keys={list(result_data.keys())}")

    return request_id, seed, image_url


st.set_page_config(page_title="RunComfy Generator", layout="centered")
st.title("RunComfy → Streamlit Cloud 이미지 생성")

# api_key = st.secrets.get("RUNCOMFY_API_KEY", "")
# deployment_id = st.secrets.get("RUNCOMFY_DEPLOYMENT_ID", "")

if not api_key or not deployment_id:
    st.error("Secrets에 RUNCOMFY_API_KEY / RUNCOMFY_DEPLOYMENT_ID를 설정해야 합니다.")
    st.stop()
