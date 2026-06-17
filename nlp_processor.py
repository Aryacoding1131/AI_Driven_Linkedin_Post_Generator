import re
import spacy

nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text


def extract_entities(text):
    doc = nlp(text)

    entities = {
        "PERSON": [],
        "ORG": [],
        "DATE": [],
    }

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    return entities


def process_certificate(text):
    cleaned = clean_text(text)
    entities = extract_entities(cleaned)

    return {
        "raw_text": text,
        "cleaned_text": cleaned,
        "entities": entities
    }