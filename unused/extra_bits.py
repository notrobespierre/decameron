#first story
URL = return_URL(1, 1)
story_string = clean_story(URL)
first = story_string

with open("0101.txt", 'w', encoding='unicode-escape') as f:
    f.write(story_string)

#third story
URL = return_URL(1, 3)
story_string = clean_story(URL)
third = story_string


with open("0103.txt", 'w', encoding='unicode-escape') as f:
    f.write(story_string)

id2word = corpora.Dictionary(texts)
corpus = [id2word.doc2bow(text) for text in texts]
#num_topics = 10
lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=10, random_state=42, passes=50, alpha="auto", per_word_topics=True)

stop_words = stopwords.words("english")
annoying_words = ["thou", "one", "said", "thy", "tis", "thee"]
stop_words += annoying_words
print(stop_words)
texts = [[word for word in simple_preprocess(str(story)) if word not in stop_words] for story in stories_all]

#first = open("0101.txt")
#third = open("0103.txt")