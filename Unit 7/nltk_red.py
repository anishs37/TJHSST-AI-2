import nltk
from nltk.corpus import *
from nltk.corpus import wordnet as wn

# Define a function find_language() that takes a string as its argument, and returns a list of languages that have 
# that string as a word. Use the udhr corpus and limit your searches to files in the Latin-1 encoding.

# def find_language(to_check):
#     latin_1_langs = []
#     return_langs = []

#     for dic in nltk.corpus.udhr.fileids():
#         if "Latin1" in dic:
#             latin_1_langs.append(dic)

#     print(latin_1_langs)

#     for lang in latin_1_langs:
#         if to_check.lower() in nltk.corpus.udhr.words(lang) or to_check.upper() in nltk.corpus.udhr.words(lang):
#             return_langs.append(lang)
    
#     print(return_langs)

# find_language("SA")

# all_synsets=wn.all_synsets('n')
# hyper_counts=[len(syn.hypernyms()) for syn in all_synsets]
# average_num_hyper=sum(hyper_counts)/len(hyper_counts)
# print("branching factor of the noun hypernym hierarchy: ",average_num_hyper)

# vsequences = set([''.join([char for char in word if char in 'aeiou']) for word in words])

# def similarity(all_pairs):
#     list_to_ret = []

#     for p in all_pairs:
#         p_sp = p.split("-")
#         word1, word2 = p_sp[0], p_sp[1]
#         synset1 = wn.synset(word1 + '.n.01')
#         synset2 = wn.synset(word2 + '.n.01')

#         ps = synset1.path_similarity(synset2)
#         list_to_ret.append((ps, p))

#     list_to_ret.sort(reverse=True)
#     print(list_to_ret)

# ap = []

# ap.append("car-automobile")
# ap.append("gem-jewel")
# ap.append("journey-voyage")
# ap.append("boy-lad")
# ap.append("coast-shore")
# ap.append("asylum-madhouse")
# ap.append("magician-wizard")
# ap.append("midday-noon")
# ap.append("furnace-stove")
# ap.append("food-fruit")
# ap.append("bird-cock")
# ap.append("bird-crane")
# ap.append("tool-implement")
# ap.append("brother-monk")
# ap.append("lad-brother")
# ap.append("crane-implement")
# ap.append("journey-car")
# ap.append("monk-oracle")
# ap.append("cemetery-woodland")
# ap.append("food-rooster")
# ap.append("coast-hill")
# ap.append("forest-graveyard")
# ap.append("shore-woodland")
# ap.append("monk-slave")
# ap.append("coast-forest")
# ap.append("lad-wizard")
# ap.append("chord-smile")
# ap.append("glass-magician")
# ap.append("rooster-voyage")
# ap.append("noon-string")

# print(similarity(ap))

# import re

# pattern = re.compile(r'[a-z]+-\n[a-z]+', re.I)

# text_to_check = 'LONG-\nterm'
# to_pr = pattern.sub(' ', text_to_check)
# print(to_pr)

words = ['attribution', 'confabulation', 'elocution',
         'sequoia', 'tenacious', 'unidirectional']
vsequences = set()
for word in words:
    vowels = []
    for char in word:
        if char in 'aeiou':
            vowels.append(char)
    vsequences.add(''.join(vowels))

print(sorted(vsequences))
vsequences = sorted(set(''.join([ch for ch in wd if(ch in 'aeiou')]) for wd in words))
print(vsequences)