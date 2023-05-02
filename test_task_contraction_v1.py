#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pytest
from task_contraction_v1 import contract

    
def test_contract_prep_art_at_the_end():
    # Test case 1: The preposition-article pair that should be contracted, is at the end of the sentence.
    assert contract("Ich gehe zu der Schule.") == "Ich gehe zur Schule."

def test_contract_prep_art_at_the_beginning():
    # Test case 2: The preposition-article pair that should be contracted, is at the beginning of the sentence \
    # check for case-sensitivity.
    assert contract ("In dem Frühsommer ziehen Tomaten in den Garten um.") == "Im Frühsommer ziehen Tomaten in den Garten um."
    
def test_contract_many_prep_art():
    #Test case 3: Sentence with many preposition-article pairs that should be contracted.
    assert contract("Zu der Schule gehe ich zuerst und danach in das Kino.") == "Zur Schule gehe ich zuerst und danach ins Kino."

def test_contract_prep_art_not_in_the_dict():
    #Test case 4: Sentence with the preposition-article pair not included in the dictionary. 
    assert contract("Neben der Schule befindet sich eine Sporthalle.") == "Neben der Schule befindet sich eine Sporthalle."
    
def test_contract_prep_art_indefinite():
    #Test case 5: Sentence with the preposition-article pair where the article is indefinite.
    assert contract("Täter dringen auf ein Gelände eines Privathauses ein.") == "Täter dringen auf ein Gelände eines Privathauses ein."
    
def test_contract_if_attribute1():
    #Test case 6: Attributsatz. #Not working
    assert contract("Ich lese ein Buch, in dem Lehrer über ihre Erfahrungen berichten.") == \
    "Ich lese ein Buch, in dem Lehrer über ihre Erfahrungen berichten."

def test_contract_if_prep_attribute():
    #Test case 7: Präpositionalattribut. #Not working
    assert contract("Ich bin hinter dem Haus von Ole.") == "Ich bin hinter dem Haus von Ole."
    
def test_contract_if_attribute2():
    #Test case 8: Attributsatz. #Not working
    assert contract("Ich bin in dem Park, wo wir uns letztes Mal getroffen haben.") == \
    "Ich bin in dem Park, wo wir uns letztes Mal getroffen haben."
    
def test_contract_if_Gen_attribute():
    #Test case 9: Genitivattribut. #Not working
    assert contract("Auf dem Gelände der Autofabrik hat es gebrannt.") == "Auf dem Gelände der Autofabrik hat es gebrannt."


# In[ ]:





# In[ ]:





# In[ ]:




