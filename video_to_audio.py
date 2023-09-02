from pydub import AudioSegment
from googletrans import Translator

def decode_and_translate_audio(video_file, output_file, target_language):
    if not output_file.endswith(".wav"):
        output_file += ".wav"
    AudioSegment.from_file(video_file).set_channels(
        1).export(output_file, format="wav")

    translator = Translator()

    # Replace this with your English transcript or load it from a file
    original_text = "Replace this with your English transcript"

    # Translate the English transcript to the target Indian regional language
    translated_text = translator.translate(original_text, dest=target_language).text
    
    return translated_text

if __name__ == "__main__":
    video_file = "input_video.mp4"  # Replace with your input video file
    output_file = "output_audio.wav"  # Replace with your desired output audio file

    # Language codes for Indian regional languages
    indian_languages = {
        "Hindi": "hi",
        "Tamil": "ta",
        "Telugu": "te",
        "Kannada": "kn",
        "Bengali": "bn",
        "Marathi": "mr",
        "Gujarati": "gu",
        "Punjabi": "pa",
        "Odia": "or",
        "Malayalam": "ml"
    }

    # Choose the target Indian regional language
    target_language = "Hindi"  # Default to Hindi

    translated_text = decode_and_translate_audio(video_file, output_file, target_language)

    print(f"Translated Text ({target_language}): {translated_text}")
