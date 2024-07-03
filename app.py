import streamlit as st
import google.generativeai as genai
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import uuid

# Configure the Gemini API key
GOOGLE_API_KEY = "AIzaSyDeotQVqEvf_W7a16B-I3hsTMmIt_XCIYc"
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
model = genai.GenerativeModel('gemini-1.5-pro')

# Streamlit app
st.title("Chat with Gemini AI 🤖 (with Translation)")

# Initialize chat history and language selection
if "messages" not in st.session_state:
    st.session_state.messages = []
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Sinhala"

# Function to translate text
def translate_text(text, target_language):
    try:
        translator = GoogleTranslator(source='auto', target=target_language)
        return translator.translate(text)
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return text  # Return original text if translation fails

# Function to generate and play audio
def text_to_speech(text, lang):
    try:
        tts = gTTS(text=text, lang=lang)
        filename = f"temp_audio_{uuid.uuid4()}.mp3"
        tts.save(filename)
        os.system(f"start {filename}")  # This works on Windows. For other OS, you might need to adjust this line.
        return filename
    except Exception as e:
        st.error(f"Text-to-speech error: {str(e)}")
        return None

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant":
            col1, col2 = st.columns([4, 1])
            with col2:
                if st.button("Read", key=f"read_{message['id']}"):
                    lang = 'si' if st.session_state.selected_language == "Sinhala" else 'ta'
                    filename = text_to_speech(message["translated_content"], lang)
                    if filename:
                        st.success("Audio playing...")

# Chat input
if prompt := st.chat_input("You:"):
    st.session_state.messages.append({"role": "user", "content": prompt, "id": str(uuid.uuid4())})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get Gemini's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            response = model.generate_content(prompt)
            original_response = response.text
            
            # Use the selected language for translation
            target_lang = 'si' if st.session_state.selected_language == "Sinhala" else 'ta'
            translated_response = translate_text(original_response, target_lang)
            
            full_response = f"Original: {original_response}\n\n{st.session_state.selected_language}: {translated_response}"
            message_placeholder.markdown(full_response)
            
            message_id = str(uuid.uuid4())
            st.session_state.messages.append({
                "role": "assistant", 
                "content": full_response, 
                "translated_content": translated_response,
                "id": message_id
            })
            
            col1, col2 = st.columns([4, 1])
            with col2:
                if st.button("Read", key=f"read_{message_id}"):
                    filename = text_to_speech(translated_response, target_lang)
                    if filename:
                        st.success("Audio playing...")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            full_response = f"An error occurred: {str(e)}"

# Sidebar for API key input and language selection
with st.sidebar:
    st.subheader("Configuration")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    if api_key:
        genai.configure(api_key=api_key)
        st.success("API Key configured successfully!")

    # Language selection
    st.session_state.selected_language = st.radio(
        "Select Translation Language:",
        ("Sinhala", "Tamil")
    )

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.experimental_rerun()

