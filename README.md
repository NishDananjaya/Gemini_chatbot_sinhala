 

 
# Gemini AI Chatbot with Translation

This is a chatbot application that uses Google's Gemini AI for generating responses and integrates translation features using the `deep_translator` library. The chatbot can translate responses into Sinhala or Tamil and also provides text-to-speech capabilities.

## Features

- Chat with Google's Gemini AI.
- Translate AI responses to Sinhala or Tamil.
- Text-to-speech functionality for translated responses.
- Streamlit-based user interface for interactive chat experience.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/gemini-ai-chatbot.git
   cd gemini-ai-chatbot
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Google API key by replacing the placeholder in the script or entering it through the Streamlit sidebar during runtime.

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open the local Streamlit server link (usually `http://localhost:8501`) in your web browser.

3. Interact with the chatbot, choose the translation language (Sinhala or Tamil) from the sidebar, and use the "Read" button to listen to the responses.

## File Structure

- `app.py`: Main application script containing the chatbot logic and Streamlit interface.
- `requirements.txt`: List of required Python packages.

## Dependencies

- `streamlit`: For creating the web interface.
- `google-generativeai`: For accessing the Gemini AI model.
- `deep_translator`: For translating text.
- `gtts`: For converting text to speech.
- `uuid`: For generating unique identifiers for chat messages.

## Configuration

- **Google API Key**: You need to configure the Google API key for the Gemini AI model. You can either set it directly in the script or input it through the Streamlit sidebar.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://developers.google.com/generative-ai)
- [deep_translator](https://pypi.org/project/deep-translator/)
- [gTTS](https://pypi.org/project/gTTS/)

## Author

- NishDananjaya
- [GitHub Profile](https://github.com/NishDananjaya)
```
