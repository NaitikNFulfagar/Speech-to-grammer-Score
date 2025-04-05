import speech_recognition as sr
import language_tool_python

def grammar_score(file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Transcribed Text:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
        
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    error_count = len(matches)
    total_words = len(text.split())
    score = max(0, 100 - (error_count / total_words) * 100)
    return round(score, 2), matches





file = "LJ001-0001.wav"
score, issues = grammar_score(file)
print("Grammar Score:", score)

score, issues = grammar_score("LJ001-0002.wav")
print("Grammar Score:", score)

score, issues = grammar_score("LJ001-0003.wav")
print("Grammar Score:", score)
