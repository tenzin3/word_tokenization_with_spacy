from word_tokenizer.word_tokenizer_spacy import (
    load_spacy_word_tokenizer,
    tokenize_english_with_named_entities,
)


def test_tokenize_english_with_named_entities():
    test_sentence = "Barack Obama has $3000 dollars."
    spacy_nlp = load_spacy_word_tokenizer()
    assert (
        tokenize_english_with_named_entities(spacy_nlp, test_sentence)
        == "Barack+Obama has $+3000+dollars . "
    )
