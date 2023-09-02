from googletrans import Translator

def transcribe_and_translate(transcripts, src_language, target_languages):
    # Initialize the translator
    translator = Translator()

    translated_transcripts = []
    for transcript in transcripts:
        translated_transcript = {}
        for lang in target_languages:
            if lang != src_language:
                # Translate to Indian regional languages
                translated_text = translator.translate(
                    transcript[src_language], src=src_language, dest=target_languages[lang]).text
                translated_transcript[lang] = translated_text
            else:
                translated_transcript[src_language] = transcript[src_language]
        translated_transcripts.append(translated_transcript)

    return translated_transcripts

if __name__ == "__main__":
    transcripts = [
        {"en": "Hello", "hi": "नमस्ते", "ta": "வணக்கம்", "kn": "ಹಲೋ", "bn": "হ্যালো"},
        {"en": "Goodbye", "hi": "अलविदा", "ta": "பிரித்தியில்", "kn": "ಗುಡ್ಬೈ", "bn": "বিদায়"},
    ]
    src_language = "en"
    target_languages = {"hi": "hi", "ta": "ta", "kn": "kn", "bn": "bn"}

    translated_transcripts = transcribe_and_translate(
        transcripts, src_language, target_languages)
    print(translated_transcripts)
