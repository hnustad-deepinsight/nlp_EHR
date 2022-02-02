Testing of NLP software i python


you can download the norwegian bokmål models with the following command:

small:
python -m spacy download nb_core_news_sm
medium:
python -m spacy download nb_core_news_md
large:
python -m spacy download nb_core_news_lg


these can then be used in python with:
import spacy

nlp = spacy.load("nb_core_news_md")
doc = nlp(sentences[0])
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)

