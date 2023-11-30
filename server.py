from flask import Flask, request, jsonify
from voice_recognition import VoiceRecognition
from nlp_processing import NLPProcessing
from machine_learning import MachineLearning

app = Flask(__name__)
voice_recognition = VoiceRecognition()
nlp_processing = NLPProcessing()
machine_learning = MachineLearning()

@app.route('/process_user_input', methods=['POST'])
def process_user_input():
    data = request.get_json()
    user_input = data.get('user_input')

    # Voice recognition
    voice_text = voice_recognition.recognize_voice()

    # NLP processing
    relevant_info = nlp_processing.process_text(user_input)

    # Machine learning response
    machine_learning_response = machine_learning.generate_response(len(relevant_info))

    response = f"Voice Text: {voice_text}, Relevant Info: {relevant_info}, ML Response: {machine_learning_response}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
