
# Simple contraction algorithm for German sentences

The objective of this project is to write an algorithm that can contract prepositions and articles in German sentences, thereby improving style and readability of the written German language. The algorithm will also detect instances where it is not possible to make a contraction and will not change the sentence.


## Assumptions:

    1. The algorithm assumes that the input sentences should be written in the Standard German language, expected in formal writing, not in colloquial language.
    2. The sentences are assumed to be grammatically correct.


## Grammar rules:

Based on the information from the dictionary of the Standard German Language "Duden", the following grammar rules are used by the algorithm to identify opportunities to contract prepositions and articles in German sentences in formal writing:

    1. The article and the preposition should be contracted if the article is definite, in the singular form, and in the accusative or dative case. These articles are *dem* , *der*, and *das*.

    2. These are certain prepositions that are able to contract with the articles. Their contraction is accepted for use in the Standard German language. These prepositions are: *an*, *auf*, *durch*, *für*, *in*, *um*, *bei*, *von*, *zu*.

    3. The contraction rule for preposition-article pairs is as follows:
        3.1. If the preposition ends with *-n* and is contracted with the article *dem*, the *-n* at the end of the preposition will be replaced by the last letter of the article: *an dem* to *am*. 
        3.2. By other prepositions, the last letter of the article will be added to the whole form of the preposition: *zu der* to *zur*.


## Usage

1. Install Python and Jupyter Notebook.
2. ``Clone the repository: git clone `https://github.com/anastasiyabortnikova/JetBrains.git`.``
3. ``Open the file: `task_contraction_v1.py`.`` ``Now you should be able to run the `contract` function.``


## Implementation details

The `contract(sentence)` function uses nested loops to iterate over the list of words in the input sentence and the dictionary of preposition-article pairs. For each preposition-article pair, the function verifies whether the preposition and article appear in sequence in the input sentence. If they do, the function replaces preposition-article pairs with their contracted form using dictionary.


## Limitations

While the `contract()` function is effective in contracting preposition-article pairs using dictionary, there are some limitations to be aware of:

    1. According to German grammar rules, not all preposition-article pairs listed in the dictionary can be contracted because of syntactic constraints imposed by sentence structure. The algorithm does not analyze the structure of the sentence. Therefore, the algorithm is limited to working only with simple sentences that contain one or more prepositional phrases without modifiers. The algorithm does not work on relative clauses: 

        > + Wir wohnen **in dem Haus**, **das** Herr Maier verkaufen will. # Modifier, contraction is not allowed.
        >
        > + Ich bin **in dem Park**, **wo** wir uns letztes Mal getroffen haben. # Modifier, contraction is not allowed.
        >
        > + Ich lese ein Buch, **in dem** Lehrer über ihre Erfahrungen berichten. # There is no prepositional phrase with the preposition-pair *in dem*, contraction is not allowed.
        
    2. The algorithm can not detect sentences where it is not possible to make a contraction without altering the meaning of the sentence. The preposition-article pair can not be contracted if the definite article is used as a demonstrative pronoun (meaning: this/that):

        > + Zu dem Arzt gehen wir nie wieder hin.
        >
        > + In dem Restaurant war ich auch noch nicht.
    
    3. The dictionary does not include certain preposition-article pairs that are able to be contracted, as these forms are rarely used and almost only found in colloquial language. These are following contracted forms: *hinters*, *übers*, *unters*, *vors*, *aufm*, *ausm*, *hinterm*, *überm*, *unterm*, *vorm*, *aufn*, *hintern*, *übern*, *untern*, *vorn*.


## Improvement suggestions

    1. To overcome these limitations, one possible option is to use Python libraries and tools that enable working with POS and syntax tags. For instance, NLTK or Spacy. By doing so, the algorithm can effectively handle sentence structure and contract preposition-article pairs based on syntactical relationships. The focus of the algorithm should be on identifying the noun as part of a prepositional phrase, along with any possible modifiers.

    2. If the sentence allows the use of colloquial expressions, the algorithm should include additional preposition-article pairs that are commonly used in colloquial language. Thus, the algorithm should also take into account the style of the text, style tags should be embedded within the code. This same principle can be used for decontraction if the contraction does not match the selected text style.


## Contributing

Contributions to this project are welcome. 


## Testing

1. Install pytest.
2. ``Clone the repository: git clone `https://github.com/anastasiyabortnikova/JetBrains.git`.``
3. ``Run the script: `test_task_contraction_v1.py` with the following command: `pytest test_task_contraction_v1.py`.``

The tests 1 to 4 have passed succesfully, while tests 5 to 7 are failing due to missing POS and syntax tags.


## License

This project is licensed under the MIT License.


## Contact

<anastasija.bortnikova@gmail.com>

