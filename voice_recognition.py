from pocketsphinx import LiveSpeech

class VoiceRecognition:
    def __init__(self):
        self.speech = LiveSpeech()

    def recognize_voice(self):
        for phrase in self.speech:
            return str(phrase)
