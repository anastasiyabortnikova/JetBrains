import pytest
from simple_algorithm import contract

    
def test_contract_prep_art_at_the_end():
    # Test case 1: tests if the algorithm contracts the preposition-article pair when the prepositional phrase is at the end of the sentence.
    assert contract("Ich gehe zu der Schule.") == "Ich gehe zur Schule."

def test_contract_prep_art_at_the_beginning():
    # Test case 2: checks case-sensitivity and tests if the algorithm contracts the preposition-article pair when the prepositional phrase is at the beginning of the sentence.
    assert contract ("In dem Frühsommer ziehen Tomaten in den Garten um.") == "Im Frühsommer ziehen Tomaten in den Garten um."
    
def test_contract_many_prep_art():
    # Test case 3: tests if the algorithm contracts multiple preposition-article pairs in one sentence.
    assert contract("Zu der Schule gehe ich zuerst und danach in das Kino.") == "Zur Schule gehe ich zuerst und danach ins Kino."

def test_contract_prep_art_not_in_dict():
    # Test case 4: tests if the algorithm contracts a preposition-article pair that is not in the dictionary. 
    assert contract("Neben der Schule befindet sich die Sporthalle.") == "Neben der Schule befindet sich die Sporthalle."
    
#tests below failing due to missing POS and syntax tags   

def test_contract_if_relative_clause_with_relative_pronoun():
    #Test case 5: shows that the algorithm does not work on a relative clause which is introduced by a relative pronoun.
    assert contract("Wir wohnen in dem Haus, das Herr Maier verkaufen will.") == "Wir wohnen in dem Haus, das Herr Maier verkaufen will."

def test_contract_if_relative_clause_with_relative_adverb():
    #Test case 6: shows that the algorithm does not work on a relative clause which is introduced by a relative adverb.
    assert contract("Ich bin in dem Park, wo wir uns letztes Mal getroffen haben.") == "Ich bin in dem Park, wo wir uns letztes Mal getroffen haben."
    
def test_contract_if_relative_clause_with_preposition_and_relative_pronoun(): 
    #Test case 7: shows that the algorithm does not work on a relative clause which is introduced by a preposition before a relative pronoun.
    assert contract("Ich lese ein Buch, in dem Lehrer über ihre Erfahrungen berichten.") == \
    "Ich lese ein Buch, in dem Lehrer über ihre Erfahrungen berichten."
    
def test_contract_if_def_art_used_as_demonstrative_pronoun():
    #Test case 8: shows that the algorithm does not work if the definite article is used as a demonstrative pronoun.
    assert contract("Zu dem Arzt gehen wir nie wieder hin.") == "Zu dem Arzt gehen wir nie wieder hin."