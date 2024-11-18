

<h3 align="center">Word Tokenizer with spacy</h3>


This package provides a word tokenizer for English text that identifies named entities like people's names and monetary values. The tokenizer joins named entities with a + sign for better differentiation.

## Code Illustration

```bash
pip install git+https://github.com/tenzin3/word_tokenization_with_spacy.git
```

```python

from word_tokenization_with_spacy.word_tokenizer_spacy import tokenize_english_with_named_entities

input = "Barack Obama has $3000 dollars."
spacy_nlp = load_spacy_word_tokenizer()

output = tokenize_english_with_named_entities(spacy_nlp, test_sentence)
assert output == "Barack+Obama has $+3000+dollars . "
```
