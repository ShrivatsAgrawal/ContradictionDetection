"""
Created on Mon Feb 11 14:02:52 2019

@author: Shrivats Agrawal
"""
import spacy
import spacyexplained
import contradiction
import Negation
#from nltk.corpus import wordnet
nlp = spacy.load('en')
#explacy.modload()


#sent1=input("Input the first sentence:")
sent1=input("Input the first sentence:")
sent2=input("Input the second sentence:")
spacyexplained.print_parse_info(nlp,sent1)
print("\n")
spacyexplained.print_parse_info(nlp,sent2)
#sent2=input("Input the second sentence:")
doc = nlp(sent1)
doc2 = nlp(sent2)
wrdlist=list()
antony=list()
contr_tracker=0

antonym_tracker=0
#for token in doc:
    #wrdlist.append(token)
''' print(token.text,"\nLEMMA: ", token.lemma_,"\nPart of Speech: ",token.pos_,"\nTAG: ", 
          token.tag_, "\nDEP: ",
          token.dep_,"\nShape: ",token.shape_,"\nIs Alphabet: ", 
          token.is_alpha,"\nIs Stop: ", token.is_stop,"\n")'''
negdoc1=0
verb1=""
verb2=""
for token in doc:
    if(token.dep_=="neg"):
        negdoc1=1
        verb1+="NOT "
    #Storing the antonyms of root words
    if(token.pos_=="VERB" and token.dep_=="ROOT"):
        print(token.text)
        verb1+=token.lemma_
        contradiction.antysyn(token.lemma_)
        for anton in contradiction.antonyms:
            antony.append(anton)
negdoc2=0
for token in doc2:
    #print(token.text,"->",token.is_stop)
    if(token.dep_=="neg"):
        negdoc2=1
        verb2+="NOT "
    if(token.pos_=="VERB" and token.dep_=="ROOT"):
        verb2+=token.lemma_
        if(token.lemma_ in antony):
            antonym_tracker=1
            

contr_tracker=Negation.checknegationcontradiction(antonym_tracker,negdoc1,negdoc2)
        
if contr_tracker==1:
    print("\n","->",verb1.upper(),"and",verb2.upper(),"can't happen simultaneously.")
    print("->THE SENTENCES CONTRADICT EACH OTHER.")
else:
    print("\nCONTRADICTION NOT FOUND")
            
        