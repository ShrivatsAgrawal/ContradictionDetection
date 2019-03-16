# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:02:52 2019

@author: Shrivats Agrawal
"""
synonyms = []
antonyms = []
#word="went"
def antysyn(word):
    from nltk.corpus import wordnet
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    #print("Synonym:",set(synonyms))
    print("Antonym:",set(antonyms))
'''antysyn("went")
print("\n\n")
antysyn("go")'''
#wn.synsets('talk.v.02').lemma_names()
