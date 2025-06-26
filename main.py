import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()

# Gemini API key configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Utilize optimal Gemini model
MODEL_NAME = "models/gemini-2.0-flash-exp"

# UI setup
st.set_page_config(page_title="AutoCircuit")
st.title("AutoCircuit")

st.markdown("### Provide Circuit Requirements")

# Initalize input fields for user
num_inputs = st.selectbox("Number of Inputs", [2, 3, 4])
behavior = st.text_input("Desired Behavior", placeholder="ex. parity checker, counter, etc.")
sync = st.checkbox("Synchronous?")

# Button to generate circuit
if st.button("Generate Circuit"):
    if not behavior:
        st.warning("Please describe the desired behavior.")
    else:
        # Gemini prompt for professional circuit generation
        prompt = f"""
You are a digital logic design assistant.

Given:
- Number of inputs: {num_inputs}
- Desired behavior: {behavior}
- Synchronous: {'Yes' if sync else 'No'}

Please provide:
1. Whether the circuit is combinational or sequential.
2. A brief explanation (1–2 lines max).
3. The logic expression or HDL-style pseudocode.
4. A minimal truth table.
5. An ASCII diagram.

Keep the output concise, professional, and free of unnecessary commentary.
"""

        try:
            model = genai.GenerativeModel(MODEL_NAME)
            response = model.generate_content(prompt)
            
            # Display Gemini's response
            st.markdown("### Circuit Description")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Could Not Generate Circuit. Error: {e}")
