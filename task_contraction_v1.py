#!/usr/bin/env python
# coding: utf-8

# In[174]:


# Rule for articles: definite, Sg, in Dative or Accusative; list of articles: ["das", "dem", "der"].
# Rule for prepositions: certain prepositions, not all, can be contracted. List of prepositions can be contracted: ["an", "auf", "bei", "durch", "für", "hinter", "in", "über", "um", "unter", "von", "vor", "zu"].
# Rule: Not every preposition from the list above can be contracted. List of Prep-Art-combination with no contraction = [("an", "der"), ("auf", "der"), ("auf", "dem"), ("bei", "der"), ("hinter", "der"), ("in", "der"), ("über", "der"), ("unter", "der"), ("von", "der"), ("vor", "der")]
# The rule ignored in this code: Syntax: No contraction if there is a modifier after the prep-art-noun.
# Contraction rule: preposition without -n at the end + last letter of the article. If preposition ends -n is contracted with dem, change -n to -m
# I assume that sentences are grammatically correct.

def contract(sentence):
    """ The function returns the sentence with contracted prepositions and articles if conditions in the loop are met. 
         sentence: A string representing the input sentence.
         return: A string representing the input sentence with contracted prepositions and articles, if conditions in the loop are met. Otherwise, the original sentence will remain with no changes.
    """
    
    words = sentence.split()  #it is a list

    prep_art_contraction = {  #comment
        ("an", "das") : "ans",
        ("an", "dem") : "am",
        ("auf", "das") : "aufs",
        ("auf", "dem") : "aufm",
        ("bei", "dem") : "beim",
        ("durch", "das") : "durchs",
        ("für", "das") : "fürs",
        ("hinter", "dem") : "hinterm",
        ("in", "dem") : "im",
        ("in", "das") : "ins",
        ("über", "das") : "übers",
        ("über", "dem") : "überm",
        ("um", "das") : "ums",
        ("unter", "das") : "unters",
        ("unter", "dem") : "unterm",
        ("von", "dem") : "vom",
        ("vor", "dem") : "vorm",
        ("zu", "dem") : "zum",
        ("zu", "der") : "zur"

    }

    
    for key in prep_art_contraction:
        x, y = key  # Unpacked the tuple in the key into two variables.
        for i in range(len(words) - 1): # comment 
            if words[i].lower() == x and words[i+1].lower() == y: # comment?
                words[i:i+2] = [prep_art_contraction[key]] # Replaced the preposition and article with the contracted form.
                    
                    
    contracted_sentence = " ".join(words) # Reconstructed the sentence from the modified list of words.
    
    return contracted_sentence[0].upper() + contracted_sentence[1:] # Returns the sentence with contracted form if conditions are met. Otherwise original sentence with no changes. Returns the capitalization of the initial letter in the sentence.



# In[ ]:





# In[ ]:





# In[ ]:




