import spacy
from spacy.lang.nb.examples import sentences

nlp = spacy.load("nb_core_news_md")
doc = nlp(sentences[0] + ' ' + sentences[1] + ' ' + sentences[2] + ' ' + sentences[3])
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)





