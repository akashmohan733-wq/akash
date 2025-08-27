import random
import streamlit as st

# Option lists
STYLES    = ["", "anime", "cyberpunk", "watercolor", "photorealistic"]
MOODS     = ["", "epic", "melancholic", "serene", "energetic"]
QUALITIES = [
    "ultra-detailed, 8K",
    "high resolution, 4K",
    "photorealistic, 16K",
    "vibrant, sharp focus"
]

def generate_art_prompt(
    subject: str,
    environment: str = "",
    composition: str = "",
    lighting: str = "",
    style: str = "",
    mood: str = "",
    medium: str = "",
    quality: str = ""
) -> str:
    parts = [subject.strip()]
    if environment:
        parts.append(f"in a {environment} setting")
    if composition:
        parts.append(f"with a {composition} composition")
    if lighting:
        parts.append(f"under {lighting} lighting")
    if style:
        parts.append(f"in {style} style")
    if mood:
        parts.append(f"evoking a {mood} mood")
    if medium:
        parts.append(f"as a {medium}")
    if quality:
        parts.append(quality)
    return ", ".join(parts)

# Initialize Streamlit page
st.set_page_config(page_title="ARTPROMPTAI", layout="centered")
st.title("🎨 ARTPROMPTAI — Prompt Generator")
st.write("Fill in your scene details or hit “Surprise Me” to randomize style, mood, and quality.")

# Initialize session state defaults
for key, default in {
    "style": STYLES[0],
    "mood": MOODS[0],
    "quality": QUALITIES[0],
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# Callback to randomize style, mood, quality
def randomize():
    st.session_state.style   = random.choice(STYLES[1:])
    st.session_state.mood    = random.choice(MOODS[1:])
    st.session_state.quality = random.choice(QUALITIES)

# “Surprise Me” button with on_click
st.button("🎲 Surprise Me", on_click=randomize)

# ——— Begin form ———
with st.form(key="prompt_form"):
    subject     = st.text_input("Subject & Action", "")
    environment = st.text_input("Environment", "")
    composition = st.selectbox("Composition", ["", "cinematic", "close-up", "wide-angle"])
    lighting    = st.selectbox("Lighting", ["", "dramatic backlight", "soft ambient", "neon glow"])
    style       = st.selectbox("Art Style", STYLES,    index=STYLES.index(st.session_state.style))
    mood        = st.selectbox("Mood",      MOODS,     index=MOODS.index(st.session_state.mood))
    medium      = st.selectbox("Medium",    ["", "digital painting", "oil on canvas", "sketch"])
    quality     = st.text_input("Quality & Resolution", value=st.session_state.quality)

    generate = st.form_submit_button("Generate Prompt")
# ——— End form ———

# Handle submission
if generate:
    if not subject.strip():
        st.error("Please enter a Subject & Action.")
    else:
        # Persist latest picks
        st.session_state.style   = style
        st.session_state.mood    = mood
        st.session_state.quality = quality

        prompt = generate_art_prompt(
            subject, environment, composition,
            lighting, style, mood,
            medium, quality
        )
        st.subheader("🖋️ Your Enhanced Prompt")
        st.code(prompt, line_numbers=False)