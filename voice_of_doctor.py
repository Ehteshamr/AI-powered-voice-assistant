# If you don't use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# Step 1a: Setup Text to Speech – TTS – model with gTTS
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import platform
import elevenlabs
from elevenlabs.client import ElevenLabs

# ElevenLabs API Key
ELEVENLABS_API_KEY = "sk_889312e6a4e680855fbcaaa0e1a8121d79d1d32ac35e1d82"

# Function for Text to Speech using gTTS with autoplay using pydub
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    try:
        sound = AudioSegment.from_mp3(output_filepath)
        play(sound)
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Test gTTS TTS function
input_text = "Im such a shitty person , I disobeyed my Lord who controls everything "
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


# Function for Text to Speech using ElevenLabs with autoplay using pydub
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

    try:
        sound = AudioSegment.from_mp3(output_filepath)
        play(sound)
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Uncomment to test ElevenLabs TTS function
# text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
