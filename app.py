# Streamlit app entry point
import streamlit as st
import requests

st.title("🎨 ArtPromptAI: Image Generator from Description")

# Step 1: User Input
user_input = st.text_area("Describe the image you want to see:")

# Step 2: Generate Prompt using Mistral via Ollama
def generate_prompt(user_text):
    system_prompt = (
        "You are a prompt engineer. Turn the user's short input into a detailed image generation prompt "
        "suitable for AI models like Stable Diffusion. Include setting, style, lighting, and mood."
    )
    payload = {
        "model": "mistral",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        "stream": False
    }
    response = requests.post("http://localhost:11434/api/chat", json=payload)
    return response.json()['message']['content']

# Step 3: Generate Image using Stable Diffusion (Optional)
# [This can be integrated later – for now, just generate the prompt]

if st.button("Generate Prompt"):
    if user_input:
        with st.spinner("Generating prompt..."):
            prompt = generate_prompt(user_input)
            st.success("Prompt Generated:")
            st.write(prompt)
    else:
        st.warning("Please enter a description first.")
