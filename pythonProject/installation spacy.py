import spacy

nlp = spacy.load("en_core_web_sm")
text = nlp("Pakistan is the beautiful country that has big mountain range in its northern areas")

for token in text:
    print(token, " | ", token.pos_, " | ", token.lemma_," | ",)