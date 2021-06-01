import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.corpus.reader.chunked import ChunkedCorpusReader
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import gutenberg, wordnet

# nltk.download()

# # Tokenizing data per sentences and words
# text = "Natural Language Processing is the task we give computers to read and understand (process) written text (natural language). By far, the most popular toolkit or API to do natural language processing is the Natural Language Toolkit for the Python programming language."
# print(nltk.sent_tokenize(text))
# print(nltk.word_tokenize(text))

# # Stop words have the benefit to simply your words dataset filtering "useless words"
# stop_words = set(nltk.corpus.stopwords.words("english"))
# words = nltk.word_tokenize(text)
# filtered_sentence = []

# # Simplying words dataset
# # for w in words:
# #     if w not in stop_words:
# #         filtered_sentence.append(w)
# # OR
# filtered_sentence = [w for w in words if not w in stop_words]
# print(filtered_sentence)

# # Removing word affixes from the end of words (i.e. 'ing')
# text = "I was taking a ride in the car."
# words = nltk.word_tokenize(text)
# ps = PorterStemmer()
# example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
# for w in example_words:
#     print(ps.stem(w))

# new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
# words = nltk.word_tokenize(new_text)
# for w in words:
#     print(ps.stem(w))

# Import G.W.Busch speech and tokenize each word and labelling them
# train_text = state_union.raw("2005-GWBush.txt")
# sample_text = state_union.raw("2006-GWBush.txt")

# custom_sent_tokenizer = PunktSentenceTokenizer(train_text) # Training model using last year's data
# tokenized =  custom_sent_tokenizer.tokenize(sample_text) # Generates list with sentences

# def process_content():
#     try:
#         for i in tokenized:
#             words = nltk.word_tokenize(i) # Separates sentences into words
#             tagged = nltk.pos_tag(words) # Creates tuples for each words in sentence, tagged with respective labels
#             # print(tagged)
#             # Chunking data with regular expression according to type of word (noun, adverb, etc.)
#             # chunkGram = r"""Chunk: {<RB.?>*<VB,?>*<NNP><NN>?} """
#             chunkGram = r"""Chunk: {<.*>+} 
#                                     }<VB.?|IN|DT|TO>+{""" # Chunk everything
#             chunkParser = nltk.RegexpParser(chunkGram)
#             chunked = chunkParser.parse(tagged)
            
#             # print(chunked)
#             chunked.draw()
#     except Exception as e:
#         print(str(e))

# process_content()

# Group by named entities (Organisations, money, person, location, etc.)
# train_text = state_union.raw("2005-GWBush.txt")
# sample_text = state_union.raw("2006-GWBush.txt")

# custom_sent_tokenizer = PunktSentenceTokenizer(train_text) # Training model using last year's data
# tokenized = custom_sent_tokenizer.tokenize(sample_text) # Generates list with sentences

# def process_content():
#     try:
#         for i in tokenized[5]:
#             words = nltk.word_tokenize(i) # Separates sentences into words
#             tagged = nltk.pos_tag(words) # Creates tuples for each words in sentence, tagged with respective labels
            
#             namedEnt = nltk.ne_chunk(tagged, binary=True) # Classify named entities
            
#             namedEnt.draw()
#     except Exception as e:
#         print(str(e))
# process_content()

# Lemmatizing is a similar operation to stemming. The major difference is that stemming can often create non-existent words
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("cats"))
# print(lemmatizer.lemmatize("cacti"))
# print(lemmatizer.lemmatize("geese"))
# print(lemmatizer.lemmatize("rocks"))
# print(lemmatizer.lemmatize("python"))
# print(lemmatizer.lemmatize("better"))
# print(lemmatizer.lemmatize("better", pos="a")) # Convert better to adjective
# print(lemmatizer.lemmatize("best", pos="a")) # Returns similar

# print(lemmatizer.lemmatize("run", pos="a"))
# print(lemmatizer.lemmatize("run", pos="v")) # Returns similar when in context

# You can access all datasets from ntlk in %AppData% installation folder via Corpora folder
# sample = gutenberg.raw("bible-kjv.txt")
# tok = sent_tokenize(sample)

# print(tok[5:15])

# WordNet is used look up words and their meaning according to their parts of speech, we can find synonyms, antonyms, and even examples of the word in use
# syns = wordnet.synsets("program")
# print(syns)

# print(syns[0].name()) # Synset
# print(syns[0].lemmas()[0].name()) # Just the word

# print(syns[0].definition()) # Definition
# print(syns[0].examples()) # Examples

# synonyms = []
# antonyms = []

# for syn in wordnet.synsets("good"):
#     for l in syn.lemmas():
#         # print("l: ", l)
#         synonyms.append(l.name())
#         if l.antonyms():
#             antonyms.append(l.antonyms()[0].name())

# print(set(synonyms))
# print(set(antonyms))

# Compares semantic similarity
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")

print(w1.wup_similarity(w2))