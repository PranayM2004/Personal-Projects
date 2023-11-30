from nltk import word_tokenize, pos_tag

class NLPProcessing:
    def process_text(self, text_input):
        # Tokenize the input text
        tokens = word_tokenize(text_input)

        # Part-of-speech tagging
        pos_tags = pos_tag(tokens)

        # Extract relevant information
        relevant_info = [word for word, pos in pos_tags if pos.startswith('N')]

        return relevant_info
