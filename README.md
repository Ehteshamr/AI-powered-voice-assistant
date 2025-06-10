
# 🧠 VoiceBot MD: AI-Powered Medical Image & Voice Diagnostic Assistant

VoiceBot MD is an interactive Gradio-based web app designed for educational and experimental use. It combines speech recognition, multimodal image analysis, and text-to-speech technologies to simulate a virtual doctor who can diagnose from uploaded images and respond to spoken queries in natural human-like voice.


## Features

- 🎙️ **Voice Input**: Users can ask medical questions using a microphone.
- 🖼️ **Image Analysis**: Upload medical images (e.g., skin conditions), and get AI-generated diagnostic insights.
- 🧠 **LLM Vision Analysis**: Powered by Groq’s fast inference with LLaMA 4 multimodal model.
- 🗣️ **Realistic Voice Output**: Get responses from the AI "doctor" using either gTTS or ElevenLabs voice synthesis.
- 🌐 **User Interface**: A clean, simple Gradio interface for smooth interaction.


## 📁 Project Structure

├── brain_of_doctor.py # Handles Groq multimodal (text + image) analysis

├── voice_of_patient.py # Records audio and converts it to text using Groq Whisper

├── voice_of_doctor.py # Converts AI text responses to speech (gTTS or ElevenLabs)

├── gradio_app.py # Main app with Gradio UI and backend integration

├── requirements.txt # List of required Python packages
├── *.jpg / *.png # Sample medical image files (e.g., acne.jpg, eczema.png)

##  ⚙️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/voicebot-md.git
cd voicebot-md
```

2. **Create virtual environment (optional but recommended)**
```bash 
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```







## 🔑 Environment Variables

You must create a .env file or directly paste the API keys in code (as shown in current implementation).

Required Keys:

**GROQ_API_KEY:** For using LLaMA/Whisper models via Groq.

**ELEVENLABS_API_KEY:** (Optional) For enhanced voice output with ElevenLabs TTS.

## 🧪 How to Run

```bash
python gradio_app.py
```

Then open the local Gradio link in your browser.

## Demo Flow

1. Record your query (e.g., "What is this red patch on my skin?")

2. Upload the corresponding image.

3. **The app:**

    Transcribes your voice to text (Whisper via Groq)

    Sends image + query to LLaMA vision model (via Groq)

    Converts the answer to speech using gTTS/ElevenLabs

4. Result: Audio + text response from the AI doctor.



