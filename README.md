
#  Contraction algorithm for German sentences using spaCy

The objective of this project is to write an algorithm that can contract prepositions and articles in German sentences, thereby improving style and readability of the written German language. The algorithm will also detect instances where it is not possible to make a contraction and will not change it.


## Assumptions:

1. The algorithm assumes that the input sentence is written in the Standard German language, expected in formal writing, not in colloquial language.
2. The sentence is assumed to be grammatically correct.


## Grammar rules:

The following grammar rules are used by the algorithm to identify opportunities to contract prepositions and articles in German sentences in formal writing:

1. Contraction of the following prepositions and articles is accepted for use in the Standard German language: prepositions (*an*, *auf*, *durch*, *für*, *in*, *um*, *bei*, *von*, *zu*), definite articles in singular in Accusative or Dative case (*dem* , *der*, and *das*). 

2. Contraction of the preposition-article-pair is imposible when a relative clause follows. 



## Usage

1. Install Python and Jupyter Notebook.
2. Install spacy, nlp = spacy.load('de_core_news_sm')
3. Clone the repository: git clone `https://github.com/anastasiyabortnikova/JetBrains.git`.
4. Open the file: `complex_algorithm_spacy.py`. Now you should be able to run the `contract` function.


## Implementation details

The `contract(sentence)` function starts with pattern matching to detect a prepositional phrase in the input sentence. The function uses nested loops to iterate over POS and dependency labels of the tokens in found prepositional phrase as well as in their nighbors. If the noun in the prepositional phrase has a relative clause that is modifying this noun, contraction does not occur. If the noun has no relative clause, the algorithm carried out contraction of found preposition-article pair with their contracted form using dictionary.


## Limitations

While the `contract()` function is effective in contracting preposition-article pairs in simple sentences, there are some limitations to be aware of:

1. The search for a relative clause followed by the noun in the prepositional phrase using `token.dep_ == "rc"` is not sufficient resulting in failing tests.

2. The algorithm can not detect sentences where it is not possible to make a contraction without altering the meaning of the sentence. The preposition-article pair can not be contracted if the definite article is used as a demonstrative pronoun (meaning: this/that):

> + Zu **dem** Arzt gehen wir nie wieder hin.

3. The script does not include information about other cases where contraction of the preposition-article-pair is obligatory. These cases are:
> + in fixed phrases: *im Sinne von*, *ans Licht bringen*.
>
> + in substantive infinitives: *Freude am Reiten*, *etwas zum Nachdenken*.
>
> + with dates and other time indications: *am 8. Mai*, *im Winter*.
>
> + in georgaphic names used with the article: *im Schwarzwald*.

4. The dictionary does not include preposition-article pairs that are able to contract, as these forms are rarely used and almost only found in colloquial language. These are following contracted forms: *hinters*, *übers*, *unters*, *vors*, *aufm*, *ausm*, *hinterm*, *überm*, *unterm*, *vorm*, *aufn*, *hintern*, *übern*, *untern*, *vorn*.


## Improvement suggestions

1. To detect relative clauses, the algorithm should check tokens in the input sentence for a relative pronoun or a local preposition that introduce relative clauses:

> + Ich bin in dem Park, **wo** wir uns letztes Mal getroffen haben, dann gehe ich in das Theater.
>
> + Wir wohnen in dem Haus, **das** Herr Maier verkaufen will.

2. Use tags related to semantics or infromation structure. 

3. Use additinal tags (named entities, date, time, substantive infinitives), use a list of fixed phrases.

4. If the sentence allows the use of colloquial expressions, the algorithm should include additional preposition-article pairs that are commonly used in colloquial language. Thus, the algorithm should also take into account the style of the text. This same principle can be used for decontraction if the contraction does not match the selected text style.


## Contributing

Contributions to this project are welcome. 


## Testing

1. Install pytest.
2. Clone the repository: git clone `https://github.com/anastasiyabortnikova/JetBrains.git`.
3. Run the script: `test_complex_algorithm_spacy.py` with the following command: `pytest test_complex_algorithm_spacy.py`.

5 of 8 tests have passed succesfully.


## License

This project is licensed under the MIT License.


## Contact

<anastasija.bortnikova@gmail.com>

