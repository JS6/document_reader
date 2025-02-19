import spacy
from base_ner_model import BaseNERModel


class NERGeneralModel(BaseNERModel):
    """
    Named Entity Recognition model for extracting general entities using spaCy.
    """

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract(self, text):
        """
        Extract named entities from the given text.
        """
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities


# Example of how to use the model
if __name__ == "__main__":
    ner_model = NERGeneralModel()
    texts = [
        "Bank XYZ proposes a 150 mio trade"
        "on FR0098765432 with a spread of ESTR+50bps",
    ]
    for text in texts:
        print(ner_model.extract(text))
