import spacy
from spacy import displacy

nlp = spacy.load("nb_core_news_md")
file = open("data/Notat1.txt", mode="r")
doc = file.read()
file.close()

nlp_doc = nlp(doc)

for sentence in nlp_doc.sents:
    print(sentence)
    print(len(sentence))

displacy.serve(nlp_doc.sents, style="dep")  # served on: http://0.0.0.0:5000/
displacy.serve(nlp_doc.sents, style="ent")  # served on: http://0.0.0.0:5000/

for token in nlp_doc:
    print(token.text, token.pos_, token.dep_)





