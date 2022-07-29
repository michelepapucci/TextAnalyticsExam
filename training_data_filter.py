import pandas
import stanza


class TrainingDataFilter:
    def __init__(self, df):
        self.data = df
        self.nlp = None

    def init_pipeline(self, lang, processors):
        self.nlp = stanza.Pipeline(lang=lang, processors=processors)

    def get_number_of_tokens(self, sentence, min_n_token=float('inf')):
        if self.nlp is None:
            self.init_pipeline('it', 'tokenize')
        doc = self.nlp(sentence)
        n_tokens = 0
        for sentence in doc.sentences:
            n_tokens += len(sentence.tokens)
            if n_tokens > min_n_token:
                return n_tokens
        return n_tokens

    def filter_short_sentences(self, min_n_token):
        for index, row in self.data.iterrows():
            if self.get_number_of_tokens(row['Sentence'], min_n_token) < min_n_token:
                self.data.drop(index, inplace=True)
            if index % 100 == 0 and index != 0:
                print(f"{index} - Processed")
        self.nlp = None

    def get_data(self):
        return self.data
