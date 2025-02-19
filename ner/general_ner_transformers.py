from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    pipeline,
)  # noqa
from base_ner_model import BaseNERModel


class NERTransformersModel(BaseNERModel):
    """
    Named Entity Recognition model for extracting general
    entities using Hugging Face transformers.
    """

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
        self.model = AutoModelForTokenClassification.from_pretrained(
            "dslim/bert-base-NER"
        )
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def extract(self, text: str) -> dict:
        """
        Extract named entities from the given text.
        """
        ner_results = self.nlp(text)
        organized_results = {"LOC": [], "PER": [], "ORG": [], "MISC": []}

        current_entity = None
        current_words = []

        for result in ner_results:
            entity_type = result["entity"].split("-")[1]
            if result["entity"].startswith("B-"):
                if current_entity:
                    organized_results[current_entity].append(
                        " ".join(current_words)
                    )  # noqa
                current_entity = entity_type
                current_words = [result["word"]]
            elif (
                result["entity"].startswith("I-")
                and current_entity == entity_type  # noqa
            ):
                current_words.append(result["word"])

        # Handle the last entity
        if current_entity:
            organized_results[current_entity].append(" ".join(current_words))  # noqa

        # Remove hash symbols from words
        for key, value in organized_results.items():
            organized_results[key] = [
                " ".join(word.split("##")) for word in value
            ]  # noqa

        return organized_results


# Example of how to use the model
if __name__ == "__main__":
    ner_model = NERTransformersModel()
    example = """11:49:05 I'll revert regarding BANK ABC
    to try to do another 200 mio at 2Y
    FR001400QV82 AVMAFC FLOAT 06/30/28
    offer 2Y EVG estr+45bps
    estr average Estr average / Quarterly interest payment"""
    print(ner_model.extract(example))
