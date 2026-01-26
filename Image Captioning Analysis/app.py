import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import numpy as np

### DO NOT EDIT IMPORTS ABOVE THIS LINE ###

# -----------------------------------------------------------------------------
# STEP 1: MODEL LOADING
# -----------------------------------------------------------------------------
@st.cache_resource
def load_caption_model():
    # Load the processor to prepare images for the model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    
    # Load the AI model itself
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

# Load the model and processor once
processor, model = load_caption_model()

# -----------------------------------------------------------------------------
# STEP 2: UI LAYOUT
# -----------------------------------------------------------------------------
# Set the app title
st.title("Image Captioning App")

# [cite_start]Display Student ID and Name (Required by homework instructions) [cite: 10]
st.write("Student ID: 150220305 | Name: Erdem Hasbek") 

# Set the sidebar header
st.sidebar.header("Parameter Settings")

# [cite_start]Set sidebar sliders for parameter tuning [cite: 11]

# [cite_start]1. Temperature: Controls the randomness of the output (Range: 0.1 - 1.5) [cite: 20]
temperature = st.sidebar.slider("Temperature", min_value=0.1, max_value=1.5, value=1.0, step=0.1)

# [cite_start]2. Max Length: Controls the maximum number of tokens/words (Range: 5 - 30) [cite: 27]
max_length = st.sidebar.slider("Max Length (Tokens)", min_value=5, max_value=30, value=20, step=1)

# [cite_start]3. Min Length: Controls the minimum number of tokens/words (Range: 3 - 20) [cite: 26]
min_length = st.sidebar.slider("Min Length (Tokens)", min_value=3, max_value=20, value=5, step=1)

# [cite_start]4. Number of Variations: Controls how many captions to generate [cite: 28]
num_variations = st.sidebar.slider("Number of Variations", min_value=1, max_value=5, value=1, step=1)
# -----------------------------------------------------------------------------
# STEP 3: MAIN PIPELINE
# -----------------------------------------------------------------------------
# Introduction text under title
st.write("Upload an image to utilize the BLIP model for generating captions.")

# File uploader for images, accepts jpg, jpeg, png
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # If an image is uploaded, display it
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Create an input box for starting text prompt (Conditional Captioning)
    text_prompt = st.text_input("Start the sentence with: (Optional)")

    # Create a button called 'Generate Caption' to trigger the AI
    if st.button("Generate Caption"):
        # Add a loading spinner here while the model is generating captions
        with st.spinner("Generating caption(s)..."):
            
            # Display a subheader 'Caption(s):'
            st.subheader("Caption(s):")
            
            # PRE-PROCESSING (Convert Image & Text to Tensors) ---
            # If user provided start_text, we pass it as 'text'. 
            # Otherwise we just pass the image.
            if text_prompt:
                inputs = processor(images=image, text=text_prompt, return_tensors="pt")
            else:
                inputs = processor(images=image, return_tensors="pt")
            
            # Create a loop that runs 'num_captions' times (based on slider)
            for i in range(num_variations):
                # Pass the inputs and parameters to generate caption(s).
                # Uses the slider values for temperature, max_length, and min_length.
                out = model.generate(
                    **inputs,
                    do_sample=True,             # Enable sampling for variety
                    temperature=temperature,    # Value from slider
                    max_length=max_length,      # Value from slider
                    min_length=min_length,      # Value from slider
                    top_k=50
                )

                # POST-PROCESSING (Decode Tensors back to Text)
                # The model gives us numbers, we need to decode them to words.
                # 'skip_special_tokens=True' removes technical tokens like [SEP] or [CLS].
                caption_text = processor.decode(out[0], skip_special_tokens=True)
            
                # Display the result(s)
                st.success(f"Caption {i+1}: {caption_text}")