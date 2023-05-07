
#  Contraction algorithm for German sentences using spaCy

The objective of this project is to write an algorithm that can contract prepositions and articles in German sentences, thereby improving style and readability of the written German language. The algorithm will also detect instances where it is not possible to make a contraction and will not change the sentence.


## Assumptions:

1. The algorithm assumes that the input sentences are written in the Standard German language, expected in formal writing, not in colloquial language.
2. The sentences are assumed to be grammatically correct.


## Grammar rules:

Based on the information from the dictionary of the Standard German Language "Duden", the following grammar rules are used by the algorithm to identify opportunities to contract prepositions and articles in German sentences in formal writing:

1. Contraction of the following prepositions and articles is accepted for use in the Standard German language: prepositions (*an*, *auf*, *durch*, *für*, *in*, *um*, *bei*, *von*, *zu*), definite articles in singular in Accusative or Dative case (*dem* , *der*, and *das*). 

2. Contraction of the preposition-article-pair is imposible:
- when a relative clause follows. The definite article functions as the demonstrative pronoun the one.
- when the definite article is used as a demonstrative pronoun (in the sense of this or that).

3. The contraction of the preposition-article-pair is obligatory:
- in fixed phrases: *im Sinne von*, *ans Licht bringen*
- in substantive infinitives: *Freude am Reiten*, *etwas zum Nachdenken*
- with dates and other time indications: *am 8. Mai*, *im Winter*
- in georgaphic names used with the article: *im Schwarzwald*


## Usage

1. Install Python and Jupyter Notebook.
2. Install spacy, nlp = spacy.load('de_core_news_sm') 
4. Clone the repository: git clone `https://github.com/anastasiyabortnikova/JetBrains.git`.
5. Open the file: `complex_algorithm_spacy.py`. Now you should be able to run the `contract` function.


## Implementation details

The `contract(sentence)` function uses nested loops to iterate over the list of words in the input sentence and the dictionary of preposition-article pairs. For each preposition-article pair, the function verifies whether the preposition and article appear in sequence in the input sentence. If they do, the function replaces preposition-article pairs with their contracted form using dictionary.


## Limitations

While the `contract()` function is effective in contracting preposition-article pairs using dictionary, there are some limitations to be aware of:

        
1. The algorithm can not detect sentences where it is not possible to make a contraction without altering the meaning of the sentence. The preposition-article pair can not be contracted if the definite article is used as a demonstrative pronoun (meaning: this/that):

> + Zu **dem** Arzt gehen wir nie wieder hin.
>
> + In **dem** Restaurant war ich auch noch nicht.
    
2. The dictionary does not include certain preposition-article pairs that are able to be contracted, as these forms are rarely used and almost only found in colloquial language. These are following contracted forms: *hinters*, *übers*, *unters*, *vors*, *aufm*, *ausm*, *hinterm*, *überm*, *unterm*, *vorm*, *aufn*, *hintern*, *übern*, *untern*, *vorn*.


## Improvement suggestions


1. If the sentence allows the use of colloquial expressions, the algorithm should include additional preposition-article pairs that are commonly used in colloquial language. Thus, the algorithm should also take into account the style of the text. This same principle can be used for decontraction if the contraction does not match the selected text style.


## Contributing

Contributions to this project are welcome. 


## Testing

1. Install pytest.
2. Clone the repository: git clone `https://github.com/anastasiyabortnikova/JetBrains.git`.
3. Run the script: `test_complex_algorithm_spacy.py` with the following command: `pytest test_complex_algorithm_spacy.py`.

The tests 1 to 4 have passed succesfully, while tests 5 to 8 are failing due to missing POS and syntax tags.


## License

This project is licensed under the MIT License.


## Contact

<anastasija.bortnikova@gmail.com>

