prog_words = {
    'variables': "Containers for storing values.",
    'constants': "Fixed variables.",
    'concatenation': "Adding strings together.",
    'string': "A series of characters.",
    'list': "A collection of items in a particular order.",
    'dictionary': "A collection of key-value pairs.",
    'boolean value': "Another name for a conditional test.",
    'tuple': "An immutable list.",
    'floats': "Number values with a decimal point.",
    'integers': "A whole number.",
}

for terms, meaning in prog_words.items():
    print("\n" + terms.title() + ": " + meaning)