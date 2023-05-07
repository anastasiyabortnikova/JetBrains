#!/usr/bin/env python
# coding: utf-8

# In[203]:


import spacy 
nlp = spacy.load("de_core_news_sm")
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

prep_art_contraction_dict = {  
    ("an", "das") : "ans",
    ("an", "dem") : "am",
    ("auf", "das") : "aufs",
    ("bei", "dem") : "beim",
    ("durch", "das") : "durchs",
    ("für", "das") : "fürs",
    ("in", "dem") : "im",
    ("in", "das") : "ins",
    ("um", "das") : "ums",
    ("von", "dem") : "vom",
    ("zu", "dem") : "zum",
    ("zu", "der") : "zur"
}

prep_phrase_pattern = [
    {"POS": "ADP", "TAG": "APPR"}, 
    {"POS": "DET", "TAG": "ART", "DEP": "nk"},
    {"POS": "NOUN", "TAG": "NN"}
]

matcher.add("PREP_PHRASE", [prep_phrase_pattern])
sentence = "Ich gehe zu der Schule, die schön ist, und danach in das Museum."
doc = nlp(sentence)
matches = matcher(doc)

# Checked if there is a match with the pattern and print found prepositional phrase(s)
if matches:
    print("Found prepositional phrase.")
    for match_id, start, end in matches:
        prep_phrase = doc[start:end].text
        print(prep_phrase)
        
# Checked if the noun in the prepositional phrase has a relative clause that is modifying this noun.
        for token in doc[start:end]:
            noun_token = None
            if token.pos_ == "NOUN":
                noun_token = token
                print(noun_token)
                break
                
        if noun_token:
            has_relative_clause = False
            for child in noun_token.children:
                if child.dep_ == "rc":
                    relative_clause = doc[child.i:]
                    has_relative_clause = True
                    print("This noun has a relative clause, contraction not possible.")
                    break
                    
# If there is no relative clause, the preposition-article-pair should be contracted.
            else: 
                for prep, art in prep_art_contraction_dict.keys():
                    if noun_token.nbor(-1).text != art and noun_token.nbor(-2).text != prep:
                        
                        
                        prep_art_pair = (noun_token.nbor(-2).text, noun_token.nbor(-1).text) #tuple
                            prep_art_pair = prep_art_contraction_dict[(prep, art)].split() #list
                            return nlp.make_doc(f" {replacement}" + doc[-1].text

                                                
                                                
                                                
 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




