def contract(sentence):
    """ The function returns the sentence with contracted prepositions and articles if conditions in the loop are met. 
         sentence: A string representing the input sentence.
         return: A string representing the input sentence with contracted prepositions and articles, if conditions in the loop are met. Otherwise, the original sentence will remain with no changes.
    """
    
    words = sentence.split()  

    prep_art_contraction = {  
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

    
    for key in prep_art_contraction:
        x, y = key  
        for i in range(len(words) - 1): 
            if words[i].lower() == x and words[i+1].lower() == y: 
                words[i:i+2] = [prep_art_contraction[key]] 
                    
                    
    contracted_sentence = " ".join(words) 
    
    return contracted_sentence[0].upper() + contracted_sentence[1:] 


