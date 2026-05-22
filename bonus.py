import stanza

stanza.download("no")
nlp = stanza.Pipeline(
    lang="no",
    processors="tokenize,pos,lemma,depparse"
)

sentences = [
    "I går kjøpte Kari boka.",
    "Kari leste den ikke."
]

for text in sentences:
    print("\nSentence:", text)
    doc = nlp(text)

    for sent in doc.sentences:
        for word in sent.words:
            head = "ROOT" if word.head == 0 else sent.words[word.head - 1].text
            print(
                f"{word.id}\t{word.text}\t{word.upos}\t"
                f"head={head}\tdeprel={word.deprel}"
            )