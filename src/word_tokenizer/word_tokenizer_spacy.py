import spacy 

def load_spacy_word_tokenizer():
    return spacy.load("en_core_web_sm")

def tokenize_english_with_named_entities(
    spacy_nlp: spacy, text: str
) -> str:
    # english word tokenizer
    doc = spacy_nlp(text)
    tokens_text = ""
    idx = 0
    while idx < len(doc):
        token = doc[idx]
        if token.ent_type_ == "":
            tokens_text += f"{token.text} "
            idx += 1
        else:
            curr_entity = token.ent_type_
            index = idx
            while index < len(doc) and doc[index].ent_type_ == curr_entity:
                index += 1
            curr_entity_word = [f"{doc[i].text}" for i in range(idx, index)]
            tokens_text += "+".join(curr_entity_word)
            idx = index
            tokens_text += " "
    return tokens_text

if __name__ == "__main__":
    spacy_nlp = load_spacy_word_tokenizer()
    test_sentence = "Barack Obama has $3000 dollars."
    print(tokenize_english_with_named_entities(spacy_nlp, test_sentence))