#!/usr/bin/env python
# coding: utf-8

# In[53]:


import spacy 
nlp = spacy.load("de_core_news_sm")
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

def contract(sentence):

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
    doc = nlp(sentence)
    matches = matcher(doc)

    contractions_made = False

    # Checked if there is a match with the pattern in prepositional phrase(s)
    if matches:
        for match_id, start, end in matches:
            prep_phrase = doc[start:end].text
        
            # Checked if the noun in the prepositional phrase has a relative clause that is modifying this noun.
            for token in doc[start:end]:
                if token.pos_ == "NOUN":
                    noun_token = token
                    if noun_token:
                        has_relative_clause = False
                        for child in noun_token.children:
                            if child.dep_ == "rc":
                                has_relative_clause = True
                                break
                        # If there is no relative clause, the preposition-article-pair can be contracted.           
                        else: 
                            for key in prep_art_contraction_dict.keys():
                                if noun_token.nbor(-1).text in key[1] and noun_token.nbor(-2).text in key[0]:
                                    contraction = prep_art_contraction_dict[(noun_token.nbor(-2).text, noun_token.nbor(-1).text)]
                                    sentence_with_contraction = doc.text[:noun_token.nbor(-2).idx] + contraction + " " + doc.text[noun_token.idx:]
                                    doc = nlp(sentence_with_contraction)
                                    contractions_made = True
    if contractions_made:
        return sentence_with_contraction
    else:
        return sentence
      
    
 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




