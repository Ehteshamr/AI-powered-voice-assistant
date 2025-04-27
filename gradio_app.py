# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#VoiceBot UI with Gradio
import os
import gradio as gr

from brain_of_doctor import encode_image, analyze_image_with_query
from voice_of_patient import record_audio, transcribe_with_groq
from voice_of_doctor import text_to_speech_with_gtts

#load_dotenv()

system_prompt="""You are a helpful and observant assistant specialized in understanding and describing images. 
Look carefully at the given image and describe what you notice in clear, simple language. 
If you can recognize objects, scenes, or activities, explain them naturally as if you are speaking to a real person, not in a robotic tone. 
Do not include any lists, numbers, or special characters unless necessary. 
Keep your response concise (no more than 2-3 sentences) and friendly. 
Start answering immediately without any preamble, and avoid mentioning that you are an AI or describing your analysis process.
"""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
                                                 audio_filepath=audio_filepath,
                                                 stt_model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model= "meta-llama/llama-4-scout-17b-16e-instruct"
)
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor =text_to_speech_with_gtts(input_text=doctor_response, output_filepath="final.mp3")

    return speech_to_text_output, doctor_response, voice_of_doctor


with gr.Blocks(theme=gr.themes.Soft()) as iface:
    gr.Markdown(
        """
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white; text-align: center;">
            <h1>🩺 Image Analysis VoiceBot</h1>
            <p>Analyze your medical images and get doctor's advice through voice and text!</p>
        </div>
        """
    )

    with gr.Row():
        with gr.Column():
            audio_filepath = gr.Audio(sources=["microphone"], type="filepath", label="🎤 Record your query")
            image_filepath = gr.Image(type="filepath", label="🖼️ Upload Medical Image")
            submit_btn = gr.Button("🚀 Submit", variant="primary")
        
        with gr.Column():
            speech_to_text_output = gr.Textbox(label="📝 Speech to Text Output", lines=3)
            doctor_response = gr.Textbox(label="🩺 Doctor's Response", lines=5)
            voice_of_doctor = gr.Audio(label="🔊 Listen to Doctor's Response")

    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_filepath, image_filepath],
        outputs=[speech_to_text_output, doctor_response, voice_of_doctor]
    )

iface.launch(debug=True)