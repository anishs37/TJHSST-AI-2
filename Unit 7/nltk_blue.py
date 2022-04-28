import nltk
from nltk.book import *
from nltk.corpus import *
from nltk.corpus import wordnet as wn
import random
from matplotlib import pyplot

# nltk.download("punkt")

# from nltk.corpus import wordnet as wn

# nltk.download('brown')
# nltk.download("cmudict")
# nltk.download("stopwords")

#nltk.download('omw-1.4')

# cfd = nltk.ConditionalFreqDist(
#     (target, fileid[:4])
#     for fileid in state_union.fileids()
#         for w in state_union.words(fileid)
#             for target in ['men', 'women', 'people']
#                 if w.lower().startswith(target))

# cfd.plot()

# print(wn.synset('computer.n.01').part_meronyms())
# print(wn.synset('computer.n.01').substance_meronyms())
# print(wn.synset('computer.n.01').member_holonyms)

# print()
# print()
# print()

# print(wn.synset('shirt.n.01').part_meronyms())
# print(wn.synset('shirt.n.01').substance_meronyms())
# print(wn.synset('shirt.n.01').member_holonyms)

print(nltk.Text(nltk.corpus.gutenberg.words('bryant-stories.txt')).concordance('however', lines=1000))
print()
print()
print(nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt')).concordance('however', lines=1000))

# adv_data=brown.words(categories='adventure')
# fic_data=brown.words(categories='fiction')


# adv_data = nltk.Text(adv_data)
# fic_data = nltk.Text(fic_data)
# #trying to find common words
# adv_data_fd = nltk.FreqDist(adv_data)
# fic_data_fd = nltk.FreqDist(fic_data)
# # print(adv_data.concordance('fun'))
# # print(fic_data.concordance('fun'))

# adv_data.plot()

# cmu_check = cmudict.entries()
# words = [word for word, pronunc in cmu_check]

# distinct_words = set(words)
# count_more = 0

# cmu_dict = cmudict.dict()

# for dw in distinct_words:
#     pronun_len = len(cmu_dict.get(dw))
    
#     if(pronun_len > 1):
#         count_more += 1

# print(len(words))
# print(count_more)

# list_stopwords = []

# for w in stopwords.words('english'):
#     list_stopwords.append(w)

# fic_data=brown.words(categories='fiction')
# most_freq_50_fd=nltk.FreqDist(fic_data)
# orig_freq_50 = []
# #fd that includes stop words

# for w in most_freq_50_fd:
#     orig_freq_50.append(w)

# for word in orig_freq_50:
#     if word.lower() in list_stopwords or not word.isalpha():
#         most_freq_50_fd.pop(word)

# print(most_freq_50_fd.most_common(50))

# bgm_list = list(nltk.bigrams(text1))
# # print(bgm_list)

# most_bg_50_fd = nltk.FreqDist(bgm_list)
# orig_bg_50 = []

# for w in most_bg_50_fd:
#     orig_bg_50.append(w)

# for word in orig_bg_50:
#     if word[0].lower() in list_stopwords or not word[0].isalpha() or word[1].lower() in list_stopwords or not word[1].isalpha():
#         most_bg_50_fd.pop(word)

# print(most_bg_50_fd.most_common(50))

# def zipfs_law(text,n):
#     text_fd=nltk.FreqDist(text)
#     text_fd_common=text_fd.most_common(n)
#     freqs=[y for x,y in text_fd_common]
#     ranks=[1/freq for freq in freqs]
#     pyplot.plot(ranks,freqs)
#     pyplot.show()

# zipfs_law(nltk.corpus.gutenberg.words('austen-sense.txt'),50)

# random_text=''
# for i in range(0,random.randrange(10000,1000000)):
#     random_text+=random.choice("abcdefg ")
# # print(random_text)
# zipfs_law(random_text.split(' '),100)

# def polysemy(group):
#     polysemy = 0
#     count = 0
#     name = ''

#     for synset in wn.all_synsets(group):
#         for lemma in synset.lemmas():
#             name = lemma.name()
#             polysemy = polysemy + len(wn.synsets(name, group))
#             count = count + 1

#     return polysemy / count

# print(polysemy('n'))

# from urllib import request
# from bs4 import BeautifulSoup
# from nltk import word_tokenize
# url = 'http://news.bbc.co.uk/'
# response = request.urlopen(url)
# raw = response.read().decode('utf8')
# raw = BeautifulSoup(raw, 'html.parser').get_text()
# tokens = word_tokenize(raw)
# print(tokens[0:9])

documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
print(documents)
#construct list of most frequent words in entire corpus, define feature extractor that simply checks whether each of these words is present in a given document
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]
#that is 2000 features
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
# print(document_features(movie_reviews.words('pos/cv957_8737.txt')))
#train classifier
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(30))